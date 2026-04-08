from framework.page_object.base.base_locator import BaseLocator


class HistoryLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('history.head_section.header')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header}"]]',
            description=f'Head section "{header}"'
        )
