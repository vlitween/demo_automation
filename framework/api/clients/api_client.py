import requests


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url) -> requests.Response:
        response = self.session.get(url, verify=False)
        return response
