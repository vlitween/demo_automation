from dataclasses import dataclass
from typing import Optional

from framework.utils.translator import Translator


@dataclass
class UniversalLocator:
    chrome_xpath: str
    android_xpath: Optional[str] = ''
    ios_xpath: Optional[str] = ''
    description: str = ''


class BaseLocator:

    def __init__(self, device):
        self.device = device

    @property
    def translator(self):
        return Translator(self.device)

    def new_locator(self, **kwargs):
        return UniversalLocator(**kwargs)
