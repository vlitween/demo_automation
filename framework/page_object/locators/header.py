from framework.page_object.base.base_locator import BaseLocator


class HeaderLocators(BaseLocator):
    def header(self):
        text = "Selenium automates browsers. That's it!"
        return self.new_locator(
            desktop_xpath=f'//h1[.="{text}"]',
            description=f'Header "{text}"'
        )
