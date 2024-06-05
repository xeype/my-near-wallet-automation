import os

import pytest
from pytest_check import check
from tests.api.utils import helper
import tests.api.utils.api_service as service


class TestAccessKeys:

    def test_view_access_key(self):
        sender_id = os.getenv("ACCOUNT_ID_1")
        private_key = os.getenv("ACCOUNT_PK_1")
        response = service.view_access_key(sender_id, helper.generate_public_key(private_key))
        assert "error" not in response
        assert "result" in response
        result = response["result"]
        assert "nonce" in result
        assert "block_hash" in result
        assert "block_height" in result
        assert "permission" in result
        assert result["permission"] == "FullAccess"

    def test_view_access_key_list(self):
        sender_id = os.getenv("ACCOUNT_ID_1")
        private_key = os.getenv("ACCOUNT_PK_1")
        public_key = helper.generate_public_key(private_key)
        response = service.view_access_key_list(sender_id)
        assert "error" not in response
        assert "result" in response
        result = response["result"]
        assert len(result["keys"]) > 1
        public_keys = [key["public_key"] for key in result["keys"]]
        assert public_key in public_keys
