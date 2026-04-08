from framework.page_object.base.base_locator import BaseLocator


class SponsorUsLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('sponsor_us.head_section.header')
        description_1 = self.translator.get_translation('sponsor_us.head_section.description_1')
        description_2 = self.translator.get_translation('sponsor_us.head_section.description_2')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[normalize-space()="{header}"] and .//p[normalize-space()="{description_1}"] and .//p[normalize-space()="{description_2}"]]',
            description=f'Head section "{header} {description_1} {description_2}"'
        )
