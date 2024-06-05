from tests.api.utils.api_helper import APIHelper

helper = APIHelper()


def view_access_key(sender_id, public_key):
    if ".testnet" not in sender_id:
        sender_id = f"{sender_id}.testnet"

    json = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "query",
        "params": {
            "request_type": "view_access_key",
            "finality": "final",
            "account_id": sender_id,
            "public_key": public_key
        }
    }
    response = helper.post(json).json()
    return response


def view_access_key_list(sender_id):
    if ".testnet" not in sender_id:
        sender_id = f"{sender_id}.testnet"
    json = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "query",
        "params": {
            "request_type": "view_access_key_list",
            "finality": "final",
            "account_id": sender_id
        }
    }
    response = helper.post(json).json()
    return response


def view_account(sender_id):
    if ".testnet" not in sender_id:
        sender_id = f"{sender_id}.testnet"
    json = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "query",
        "params": {
            "request_type": "view_account",
            "finality": "final",
            "account_id": sender_id
        }
    }
    response = helper.post(json).json()
    return response


def view_account_changes(account_ids, block_id):
    for index, account_id in enumerate(account_ids):
        if ".testnet" not in account_id:
            account_id = f"{account_id}.testnet"
            account_ids[index] = account_id
    json = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "EXPERIMENTAL_changes",
        "params": {
            "changes_type": "account_changes",
            "account_ids": account_ids,
            "block_id": block_id
        }
    }
    response = helper.post(json).json()
    return response


def send_transaction(signed_transaction_base64):
    json = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "send_tx",
        "params": {
            "signed_tx_base64": signed_transaction_base64,
            "wait_until": "INCLUDED_FINAL"
        }
    }
    response = helper.post(json).json()
    return response
