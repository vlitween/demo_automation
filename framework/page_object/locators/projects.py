from framework.page_object.base.base_locator import BaseLocator


class ProjectsPageLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('projects.head_section.header')
        description = self.translator.get_translation('projects.head_section.description')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header}"] and .//p[.="{description}"]]',
            description=f'Head section "{header} {description}"'
        )

    def projects_list_item(self, section_title: str):
        return self.new_locator(
            chrome_xpath=f'//div[contains(@class, "row") and .//h2[.="{section_title}"]]',
            description=f'Projects list section "{section_title}"'
        )

    @property
    def project_image(self):
        return self.new_locator(
            chrome_xpath='.//img',
            description='Project section image'
        )

    def project_header_title(self, header_title: str):
        return self.new_locator(
            chrome_xpath=f'.//h2[.="{header_title}"]',
            description=f'Project section header title "{header_title}"'
        )

    def project_header_description(self, header_description: str):
        return self.new_locator(
            chrome_xpath=f'.//p[contains(@class, "pb-5") and normalize-space()="{header_description}"]',
            description=f'Project section header description "{header_description}"'
        )

    def project_feature(self, feature_title: str, feature_description: str):
        return self.new_locator(
            chrome_xpath=f'.//*[contains(@class, "alert-heading") and normalize-space()="{feature_title}" and following-sibling::p[1][normalize-space()="{feature_description}"]]',
            description=f'Project feature "{feature_title} {feature_description}"'
        )

    def project_link(self, link_text: str):
        return self.new_locator(
            chrome_xpath=f'.//a[normalize-space()="{link_text}"]',
            description=f'Project link "{link_text}"'
        )
