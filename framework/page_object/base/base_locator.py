from dataclasses import dataclass
from typing import Optional


@dataclass
class UniversalLocator:
    desktop_xpath: str
    android_xpath: Optional[str] = ''
    ios_xpath: Optional[str] = ''
    description: Optional[str] = ''


class BaseLocator:

    def new_locator(self, **kwargs):
        return UniversalLocator(**kwargs)
