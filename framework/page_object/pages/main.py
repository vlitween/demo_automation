import i18n

from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.main import MainPageLocators
from framework.page_object.pages.components.footer import Footer
from framework.page_object.pages.components.header import Header


class MainPage(BasePage):
    @property
    def locators(self):
        return MainPageLocators()

    @property
    def header(self):
        return Header(self.device)

    @property
    def footer(self):
        return Footer(self.device)

    def check_main_page(self):
        self.actions.wait_page_title(i18n.t('main.page_title'))
        self.actions.check_item_exists(self.locators.header_1)
