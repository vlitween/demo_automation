from json import loads
from typing import Type, TypeVar

from pydantic import BaseModel
from python_json_config import Config
from requests import Response

from framework.api.clients.api_client import ApiClient

T = TypeVar('T', bound=BaseModel)


class BaseApi:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, config: Config):
        self.client = ApiClient()
        self.config = config

    @property
    def api_endpoint(self):
        return self.config.api.endpoint

    def build_url(self, endpoint):
        url = f'{self.api_endpoint}{endpoint}'
        return url

    def parse_endpoint(self, url):
        endpoint = url.split(self.api_endpoint)[-1]
        return endpoint

    def get(self, endpoint: str, response_model: Type[T], expected_status_code: int = 200, expected_latency: int = None) -> T:
        if endpoint.startswith('/'):
            url = self.build_url(endpoint)
        else:
            url = endpoint
        response = self.client.get(url)
        self.base_check(response, expected_status_code=expected_status_code, expected_latency=expected_latency)
        return response_model(**response.json())

    def base_check(self, response: Response, expected_status_code: int = 200, expected_latency: int = None):
        self.check_response_status(response, expected_status_code)
        self.check_response_content_type(response)
        self.check_response_content_presence(response)
        self.check_response_latency(response, expected_latency=expected_latency)

    @staticmethod
    def check_response_status(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, f'Expected {expected_status_code} but got {actual_status_code} for {response.url}'

    def check_response_latency(self, response: Response, expected_latency: int = None):
        if not expected_latency:
            expected_latency = self.config.api.response_latency_threshhold
        actual_latency = int(response.elapsed.microseconds / 1000)
        assert actual_latency < expected_latency, f'Expected latency threshold {expected_latency} but got {actual_latency} for {response.url}'

    @staticmethod
    def check_response_content_type(response: Response):
        actual_content_type = response.headers['content-type']
        assert actual_content_type == 'application/json', f'Actual content type {actual_content_type} should be "application/json" for {response.url}'

    def check_response_content_presence(self, response: Response):
        actual_content = self.get_response_content(response)
        assert isinstance(actual_content, dict) and actual_content, f'Invalid response content {actual_content} of {response.url}'

    @staticmethod
    def get_response_content(response: Response):
        content = loads(response.content)
        return content
