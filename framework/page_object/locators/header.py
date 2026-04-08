from framework.page_object.base.base_locator import BaseLocator


class HeaderLocators(BaseLocator):
    @property
    def header(self):
        return self.new_locator(
            chrome_xpath='//header',
            description='Header'
        )

    @property
    def logo(self):
        return self.new_locator(
            chrome_xpath='//header//a[contains(@class, "navbar-brand")]',
            description='Header logo'
        )

    def _navbar_button(self, button_text):
        return self.new_locator(
            chrome_xpath=f'//div[@id="main_navbar"]//a[contains(@class, "nav-link") and .="{button_text}"]',
            description=f'Header navbar button "{button_text}"'
        )

    @property
    def navbar_about_button(self):
        button_text = self.translator.get_translation('header.navbar.about')
        return self._navbar_button(button_text)

    @property
    def navbar_downloads_button(self):
        button_text = self.translator.get_translation('header.navbar.downloads')
        return self._navbar_button(button_text)

    @property
    def navbar_documentation_button(self):
        button_text = self.translator.get_translation('header.navbar.documentation')
        return self._navbar_button(button_text)

    @property
    def navbar_projects_button(self):
        button_text = self.translator.get_translation('header.navbar.projects')
        return self._navbar_button(button_text)

    @property
    def navbar_support_button(self):
        button_text = self.translator.get_translation('header.navbar.support')
        return self._navbar_button(button_text)

    @property
    def navbar_blog_button(self):
        button_text = self.translator.get_translation('header.navbar.blog')
        return self._navbar_button(button_text)

    def navbar_language_button(self, expected_language=None):
        if expected_language:
            return self._navbar_button(expected_language)
        else:
            return self.new_locator(
                chrome_xpath=f'(//div[@id="main_navbar"]//a[contains(@class, "nav-link")])[last()]',
                description='Language selection button'
            )

    @property
    def search_button(self):
        search_text = self.translator.get_translation('header.search')
        return self.new_locator(
            chrome_xpath=f'//div[@id="docsearch-1" and .//span[.="{search_text}"]]',
            description='Search button'
        )

    @property
    def about_dropdown(self):
        about_button_text = self.translator.get_translation('header.navbar.about')
        return self.new_locator(
            chrome_xpath=f'//header//li[.//a[normalize-space()="{about_button_text}"]]//div[contains(@class, "dropdown-menu")]',
            description='About navigation dropdown'
        )

    def about_dropdown_link(self, link_text):
        about_button_text = self.translator.get_translation('header.navbar.about')
        return self.new_locator(
            chrome_xpath=f'//header//li[.//a[normalize-space()="{about_button_text}"]]//div[contains(@class, "dropdown-menu")]//a[normalize-space()="{link_text}"]',
            description=f'About dropdown link "{link_text}"'
        )

    @property
    def announcement_banner(self):
        banner_text = f'{self.translator.get_translation('header.announcement.description')} {self.translator.get_translation('header.announcement.registration_link')}'
        return self.new_locator(
            chrome_xpath=f'//section[@id="announcement-banner" and normalize-space()="{banner_text}"]',
            description=f'Announcement section "{banner_text}"'
        )

    @property
    def announcement_banner_registration_link(self):
        link_text = self.translator.get_translation('header.announcement.registration_link')
        return self.new_locator(
            chrome_xpath=f'//section[@id="announcement-banner"]//a[normalize-space()="{link_text}"]',
            description=f'Announcement section link "{link_text}"'
        )
