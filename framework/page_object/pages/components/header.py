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

    def click_about_button(self):
        self.actions.click_element(self.locators.navbar_about_button)

    def check_about_dropdown_buttons(self):
        expected_buttons = [
            self.translator.get_translation('header.navbar.about_buttons.about_selenium'),
            self.translator.get_translation('header.navbar.about_buttons.structure'),
            self.translator.get_translation('header.navbar.about_buttons.events'),
            self.translator.get_translation('header.navbar.about_buttons.ecosystem'),
            self.translator.get_translation('header.navbar.about_buttons.history'),
            self.translator.get_translation('header.navbar.about_buttons.get_involved'),
            self.translator.get_translation('header.navbar.about_buttons.sponsors'),
            self.translator.get_translation('header.navbar.about_buttons.sponsor_us')
        ]
        for button in expected_buttons:
            self.actions.check_item_exists(self.locators.about_dropdown_link(button), should_be_visible=True)

    def click_about_selenium_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.about_selenium')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_structure_and_governance_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.structure')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_events_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.events')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_ecosystem_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.ecosystem')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_history_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.history')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_get_involved_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.get_involved')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_sponsors_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.sponsors')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_sponsor_us_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.sponsor_us')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)

    def click_downloads_button(self):
        self.actions.click_element(self.locators.navbar_downloads_button)

    def click_documentation_button(self):
        self.actions.click_element(self.locators.navbar_documentation_button)

    def click_projects_button(self):
        self.actions.click_element(self.locators.navbar_projects_button)

    def click_support_button(self):
        self.actions.click_element(self.locators.navbar_support_button)

    def click_blog_button(self):
        self.actions.click_element(self.locators.navbar_blog_button)

    def click_logo(self):
        self.actions.click_element(self.locators.logo)
