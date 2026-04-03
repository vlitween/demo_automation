from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.header import HeaderLocators


class Header(BasePage):
    @property
    def locators(self):
        return HeaderLocators()
