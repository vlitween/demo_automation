from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.header import HeaderLocators


class Header(BasePage):
    def __init__(self, device, translation_supported=False):
        super().__init__(device)
        self.translation_supported = translation_supported

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
        expected_language = self.translator.get_language_by_locale(self.device.locale) if self.translation_supported\
            else self.translator.get_language_by_locale('en')
        self.actions.check_item_exists(self.locators.navbar_language_button(expected_language))
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

    # Since all pages except Main and Documentation are not translated to other languages,
    # clicking nav buttons except Documentation and Logo (leads to Main) will automatically set default locale "en"
    # for the device

    def click_about_selenium_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.about_selenium')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_structure_and_governance_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.structure')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_events_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.events')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_ecosystem_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.ecosystem')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_history_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.history')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_get_involved_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.get_involved')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_sponsors_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.sponsors')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_sponsor_us_button(self):
        button_text = self.translator.get_translation('header.navbar.about_buttons.sponsor_us')
        self.actions.click_element(self.locators.about_dropdown_link(button_text), should_be_visible=True)
        self.translator.set_default_locale()

    def click_downloads_button(self):
        self.actions.click_element(self.locators.navbar_downloads_button)
        self.translator.set_default_locale()

    def click_documentation_button(self):
        self.actions.click_element(self.locators.navbar_documentation_button)

    def click_projects_button(self):
        self.actions.click_element(self.locators.navbar_projects_button)
        self.translator.set_default_locale()

    def click_support_button(self):
        self.actions.click_element(self.locators.navbar_support_button)
        self.translator.set_default_locale()

    def click_blog_button(self):
        self.actions.click_element(self.locators.navbar_blog_button)
        self.translator.set_default_locale()

    def click_language_button(self):
        self.actions.click_element(self.locators.navbar_language_button())

    def click_logo(self):
        self.actions.click_element(self.locators.logo)

    def check_presence_language_selection_dropdown(self):
        expected_language = self.translator.get_language_by_locale(self.device.locale) if self.translation_supported \
            else self.translator.get_language_by_locale('en')
        return self.actions.check_item_exists(self.locators.language_selection_dropdown(expected_language), should_be_visible=True)

    def select_language(self, target_language):
        language_dropdown = self.check_presence_language_selection_dropdown()
        self.actions.click_element(self.locators.language_dropdown_item(target_language), parent_element=language_dropdown)
