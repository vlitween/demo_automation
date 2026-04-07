from framework.page_object.base.base_locator import BaseLocator


class FooterLocators(BaseLocator):
    @property
    def footer(self):
        return self.new_locator(
            chrome_xpath='//footer',
            description='Footer'
        )

    def _footer_link(self, aria_label, fa_id):
        return self.new_locator(
            chrome_xpath=f'//footer//a[@aria-label="{aria_label}" and .//i[contains(@class, "{fa_id}")]]',
            description=f'Footer icon "{aria_label}"'
        )

    @property
    def linkedin_icon(self):
        return self._footer_link('Selenium Linkedin', 'fa-linkedin-in')

    @property
    def x_icon(self):
        return self._footer_link('Selenium X', 'fa-twitter')

    @property
    def community_youtube_icon(self):
        return self._footer_link('Selenium Community YouTube Channel', 'fa-youtube')

    @property
    def mastodon_icon(self):
        return self._footer_link('Selenium Mastodon', 'fa-mastodon')

    @property
    def bluesky_icon(self):
        return self._footer_link('Selenium BlueSky', 'fa-bluesky')

    @property
    def mailing_list_icon(self):
        return self._footer_link('User mailing list', 'fa-mail-bulk')

    @property
    def youtube_channel_icon(self):
        return self._footer_link('SeleniumConf YouTube Channel', 'fa-youtube')

    @property
    def software_freedom_conservancy_icon(self):
        return self._footer_link('Software Freedom Conservancy', 'fa-envelope-square')

    @property
    def github_icon(self):
        return self._footer_link('GitHub', 'fa-github')

    @property
    def slack_icon(self):
        return self._footer_link('Slack', 'fa-slack')

    @property
    def irc_icon(self):
        return self._footer_link('IRC', 'fa-comments')

    @property
    def all_rights_reserved_label(self):
        text = self.translator.get_translation('footer.all_rights_reserved')
        return self.new_locator(
            chrome_xpath=f'//footer//small[.="{text}"]',
            description=f'Footer label "{text}"'
        )

    @property
    def about_selenium_link(self):
        text = self.translator.get_translation('footer.about_selenium')
        return self.new_locator(
            chrome_xpath=f'//footer//a[.="{text}"]',
            description=f'Footer link "{text}"'
        )
