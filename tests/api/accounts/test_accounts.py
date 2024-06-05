import os

import tests.api.utils.api_service as service


class TestAccounts:

    def test_view_account(self):
        sender_id = os.getenv("ACCOUNT_ID_1")
        response = service.view_account(sender_id)
        assert "error" not in response
        assert "result" in response
        result = response["result"]
        assert "amount" in result
        assert "block_hash" in result
        assert "block_height" in result
        assert "locked" in result
        assert "storage_paid_at" in result
        assert "storage_usage" in result

    def test_view_account_changes(self):
        account_ids = [os.getenv("ACCOUNT_ID_1"), os.getenv("ACCOUNT_ID_2")]
        block_id = 165437496
        response = service.view_account_changes(account_ids, block_id)
        assert "error" not in response
        assert "result" in response
        changes = response["result"]["changes"]
        assert any(change["cause"]["tx_hash"] == "9bS2b2j6yFRw8q2kJAdvQmhhxRqBug9cnK84WQbmAwq6"
                   for change in changes)
