from framework.page_object.base.base_locator import BaseLocator


class SupportProjectLocators(BaseLocator):
    @property
    def title(self):
        title = self.translator.get_translation('support_project.title')
        return self.new_locator(
            chrome_xpath=f'//h2[.="{title}"]',
            description=f'Title "{title}"'
        )

    @property
    def description(self):
        description = self.translator.get_translation('support_project.description')
        return self.new_locator(
            chrome_xpath=f'//p[.="{description}"]',
            description=f'Description "{description}"'
        )

    @property
    def learn_more_link(self):
        link_text = self.translator.get_translation('support_project.learn_more_link')
        return self.new_locator(
            chrome_xpath=f'//a[normalize-space()="{link_text}"]',
            description=f'Link "{link_text}"'
        )
