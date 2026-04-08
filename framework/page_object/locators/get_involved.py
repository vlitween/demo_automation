from framework.page_object.base.base_locator import BaseLocator


class GetInvolvedLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('get_involved.head_section.header')
        description = self.translator.get_translation('get_involved.head_section.description')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[normalize-space()="{header}"] and .//p[normalize-space()="{description}"]]',
            description=f'Head section "{header} {description}"'
        )
