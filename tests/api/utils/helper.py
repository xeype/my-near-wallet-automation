import base64

import base58
from ed25519 import SigningKey
from py_near_primitives import TransferAction


def generate_public_key(private_key):
    if isinstance(private_key, str):
        pk = base58.b58decode(private_key.replace("ed25519:", ""))
        private_key = SigningKey(pk)
        public_key = base58.b58encode(private_key.get_verifying_key().to_bytes()).decode("utf-8")
        public_key = f"ed25519:{public_key}"
        return public_key


def decode_key(key):
    if isinstance(key, str):
        return base58.b58decode(key.replace("ed25519:", ""))
    else:
        return key


def decode_base58(value):
    return base58.b58decode(value.encode("utf8"))


def encode_base64(value):
    return base64.b64encode(value).decode("utf-8")


def create_transfer_action(amount):
    return TransferAction(amount)
