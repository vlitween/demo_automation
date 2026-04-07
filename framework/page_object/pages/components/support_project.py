import allure

from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.support_project import \
    SupportProjectLocators


class SupportProject(BasePage):
    @property
    def locators(self):
        return SupportProjectLocators(self.device)

    def check_presence_partners_and_sponsors_section(self):
        with allure.step('Scroll to Support Project section'):
            title = self.actions.check_item_exists(self.locators.title)
            self.actions.scroll_to_element(title)
        with allure.step('Check presence Support Project title'):
            self.actions.check_item_exists(self.locators.title)
        with allure.step('Check presence Support Project description'):
            self.actions.check_item_exists(self.locators.description)
        with allure.step('Check presence Learn more link'):
            self.actions.check_item_exists(self.locators.learn_more_link)
