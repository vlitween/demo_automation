from framework.page_object.base.base_locator import BaseLocator


class StructureAndGovernanceLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('structure_and_governance.head_section.header')
        description_1 = self.translator.get_translation('structure_and_governance.head_section.description_1')
        description_2 = self.translator.get_translation('structure_and_governance.head_section.description_2')
        description_3 = self.translator.get_translation('structure_and_governance.head_section.description_3')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header}"] and .//p[normalize-space()="{description_1}"] and .//p[normalize-space()="{description_2}"] and .//p[normalize-space()="{description_3}"]]',
            description=f'Head section "{header} {description_1} {description_2} {description_3}"'
        )
