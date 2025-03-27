import requests
import yaml

class RequestManager:
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            self.config = yaml.safe_load(f)
        self.base_url = self.config["base_url"]
        self.headers = {"Authorization": f"Bearer {self.config['auth_token']}"}

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}/{endpoint}", headers=self.headers, params=params)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)

    def put(self, endpoint, data=None):
        return requests.put(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
