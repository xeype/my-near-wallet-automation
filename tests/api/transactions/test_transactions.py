import os

import ed25519
from py_near_primitives import Transaction
from tests.api.utils import helper
import tests.api.utils.api_service as service


class TestTransactions:

    def test_send_transaction(self):
        sender_id = os.getenv("ACCOUNT_ID_1")
        receiver_id = os.getenv("ACCOUNT_ID_2")
        sender_private_key = os.getenv("ACCOUNT_PK_1")
        sender_public_key = helper.generate_public_key(sender_private_key)

        response = service.view_access_key(sender_id, sender_public_key)
        assert "error" not in response

        result = response["result"]
        nonce = result["nonce"] + 1
        recent_block_hash = result["block_hash"]
        pk = helper.decode_key(sender_private_key)
        private_key = ed25519.SigningKey(pk)
        actions = [helper.create_transfer_action(100000000000000010000000)]
        recent_block_hash_bytes = helper.decode_base58(recent_block_hash)

        transaction = Transaction(
            f"{sender_id}.testnet",
            private_key.get_verifying_key().to_bytes(),
            nonce,
            f"{receiver_id}.testnet",
            recent_block_hash_bytes,
            actions,
        )
        signed_trx = bytes(bytearray(transaction.to_vec(pk)))
        signed_trx_base64 = helper.encode_base64(signed_trx)
        response = service.send_transaction(signed_trx_base64)
        assert 'error' not in response
        transaction = response["result"]["transaction"]
        assert transaction["signer_id"] == f"{sender_id}.testnet"
        assert transaction["public_key"] == helper.generate_public_key(sender_private_key)
        assert transaction["nonce"] == nonce
        assert transaction["receiver_id"] == f"{receiver_id}.testnet"
        assert transaction["actions"][0]["Transfer"]["deposit"] == "100000000000000010000000"
        transaction_outcome = response["result"]["transaction_outcome"]
        assert transaction_outcome["outcome"]["executor_id"] == f"{sender_id}.testnet"
        receipts_outcome = response["result"]["receipts_outcome"]
        assert receipts_outcome[0]["outcome"]["executor_id"] == f"{receiver_id}.testnet"
