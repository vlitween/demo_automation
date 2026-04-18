import framework.utils.checks as ch
from framework.page_object.base.actions.android_actions import AndroidActions
from framework.page_object.base.actions.ios_actions import IOSActions
from framework.page_object.base.actions.playwright_actions import \
    PlaywrightActions
from framework.page_object.base.actions.selenium_actions import SeleniumActions
from framework.utils.translator import Translator


def get_actions(device):
    device_type = device.device_type
    if device_type == 'selenium':
        return SeleniumActions(device)
    elif device_type == 'playwright':
        return PlaywrightActions(device)
    elif device_type == 'android':
        return AndroidActions(device)
    elif device_type == 'ios':
        return IOSActions(device)
    else:
        return None


class BasePage:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    url = None

    def __init__(self, device):
        self.device = device
        self.actions = get_actions(device)
        self.checks = ch
        self.translator = Translator(device)

    def check_page_url(self, expected_end: str = None):
        actual_url = self.actions.get_page_url()
        expected_url = self.url + expected_end if expected_end else self.url
        self.checks.verify_strings(actual_url, expected_url)

    def open_page(self):
        self.actions.open_url(self.url)
