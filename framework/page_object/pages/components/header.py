from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.header import HeaderLocators


class Header(BasePage):
    @property
    def locators(self):
        return HeaderLocators(self.device)

    def scroll_to_header(self):
        header = self.actions.check_item_exists(self.locators.header)
        self.actions.scroll_to_element(header)

    def check_presence(self):
        self.scroll_to_header()
        self.actions.check_item_exists(self.locators.logo)
        self.actions.check_item_exists(self.locators.navbar_about_button)
        self.actions.check_item_exists(self.locators.navbar_downloads_button)
        self.actions.check_item_exists(self.locators.navbar_documentation_button)
        self.actions.check_item_exists(self.locators.navbar_projects_button)
        self.actions.check_item_exists(self.locators.navbar_support_button)
        self.actions.check_item_exists(self.locators.navbar_blog_button)
        self.actions.check_item_exists(self.locators.navbar_language_button())
        self.actions.check_item_exists(self.locators.search_button)
        self.actions.check_item_exists(self.locators.announcement_banner)
