from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.footer import FooterLocators


class Footer(BasePage):
    def __init__(self, device, translation_supported=False):
        super().__init__(device)
        self.translation_supported = translation_supported

    @property
    def locators(self):
        return FooterLocators(self.device)

    def scroll_to_footer(self):
        footer = self.actions.find_element(self.locators.footer)
        self.actions.scroll_to_element(footer, to_top=False)

    def check_presence(self):
        if not self.translation_supported:
            initial_locale = self.device.locale
            self.translator.set_default_locale()
        else:
            initial_locale = None
        self.scroll_to_footer()
        self.actions.check_item_exists(self.locators.linkedin_icon)
        self.actions.check_item_exists(self.locators.x_icon)
        self.actions.check_item_exists(self.locators.community_youtube_icon)
        self.actions.check_item_exists(self.locators.mastodon_icon)
        self.actions.check_item_exists(self.locators.bluesky_icon)
        self.actions.check_item_exists(self.locators.mailing_list_icon)
        self.actions.check_item_exists(self.locators.youtube_channel_icon)
        self.actions.check_item_exists(self.locators.all_rights_reserved_label)
        self.actions.check_item_exists(self.locators.about_selenium_link)
        self.actions.check_item_exists(self.locators.software_freedom_conservancy_icon)
        self.actions.check_item_exists(self.locators.github_icon)
        self.actions.check_item_exists(self.locators.slack_icon)
        self.actions.check_item_exists(self.locators.irc_icon)
        if initial_locale:
            self.translator.set_locale(initial_locale)
