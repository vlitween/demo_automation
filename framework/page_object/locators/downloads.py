from framework.page_object.base.base_locator import BaseLocator


class DownloadsLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('downloads.head_section.header')
        description_1 = self.translator.get_translation('downloads.head_section.description_1')
        description_2 = self.translator.get_translation('downloads.head_section.description_2')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header}"] and .//p[.="{description_1}"] and .//p[.="{description_2}"]]',
            description=f'Head section "{header} {description_1} {description_2}"'
        )
