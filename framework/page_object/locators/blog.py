from framework.page_object.base.base_locator import BaseLocator


class BlogLocators(BaseLocator):
    @property
    def head_section(self):
        header = self.translator.get_translation('blog.head_section.header')
        description = self.translator.get_translation('blog.head_section.description')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header}"] and .//p[.="{description}"]]',
            description=f'Head section "{header} {description}"'
        )
