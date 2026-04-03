from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.footer import FooterLocators


class Footer(BasePage):
    @property
    def locators(self):
        return FooterLocators()
