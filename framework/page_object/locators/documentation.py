from framework.page_object.base.base_locator import BaseLocator


class DocumentationLocators(BaseLocator):
    def article_title(self, expected_title: str):
        return self.new_locator(
            chrome_xpath=f'//div[contains(@class, "td-content")]//h1[.="{expected_title}"]',
            description=f'Documentation article title "{expected_title}"'
        )

    @property
    def documentation_content_sidebar(self):
        return self.new_locator(
            chrome_xpath='//ul[contains(@class, "td-sidebar-nav__section")]',
            description=f'Documentation content sidebar'
        )
