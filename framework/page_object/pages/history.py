import allure

import variables
from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.history import HistoryLocators
from framework.page_object.pages.components.footer import Footer
from framework.page_object.pages.components.header import Header
from framework.page_object.pages.components.partners_and_sponsors import \
    PartnersAndSponsors
from framework.page_object.pages.components.support_project import \
    SupportProject


class HistoryPage(BasePage):
    url = f'{variables.MAIN_URL}/history/'

    @property
    def locators(self):
        return HistoryLocators(self.device)

    @property
    def header(self):
        return Header(self.device)

    @property
    def footer(self):
        return Footer(self.device)

    @property
    def partners_and_sponsors(self):
        return PartnersAndSponsors(self.device)

    @property
    def support_project(self):
        return SupportProject(self.device)

    def check_page_presence(self, fast_check=False):
        with allure.step('Wait page title'):
            self.actions.wait_page_title(self.translator.get_translation('history.page_title'))
        with allure.step('Check page url'):
            self.check_page_url()
        with allure.step('Check page header'):
            self.header.check_presence()
        with allure.step('Check head section'):
            self.check_presence_head_section()
        if fast_check:
            return

    def check_presence_head_section(self):
        self.actions.check_item_exists(self.locators.head_section)
