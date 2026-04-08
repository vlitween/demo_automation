import allure

import variables
from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.documentation import DocumentationLocators
from framework.page_object.pages.components.footer import Footer
from framework.page_object.pages.components.header import Header
from framework.page_object.pages.components.partners_and_sponsors import \
    PartnersAndSponsors
from framework.page_object.pages.components.support_project import \
    SupportProject


class DocumentationPage(BasePage):
    url = f'{variables.MAIN_URL}/documentation/'

    @property
    def locators(self):
        return DocumentationLocators(self.device)

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

    def check_page_presence(self, article_title: str = 'The Selenium Browser Automation Project', article_url: str = '', fast_check=False):
        with allure.step('Wait page title'):
            self.actions.wait_page_title(f'{article_title} {self.translator.get_translation('documentation.page_title')}')
        with allure.step('Check page url'):
            self.url += article_url
            self.check_page_url()
        with allure.step('Check page header'):
            self.header.check_presence()
        with allure.step('Check article title'):
            self.actions.check_item_exists(self.locators.article_title(article_title))
        with allure.step('Check presence content sidebar'):
            self.actions.check_item_exists(self.locators.documentation_content_sidebar)
        if fast_check:
            return
