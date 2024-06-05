import requests


class APIHelper:
    def __init__(self):
        self.base_url = "https://rpc.testnet.near.org"

    def post(self, json=None):
        response = requests.post(self.base_url, json=json)
        return response
