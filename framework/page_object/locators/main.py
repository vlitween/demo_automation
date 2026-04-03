import i18n

from framework.page_object.base.base_locator import BaseLocator


class MainPageLocators(BaseLocator):
    @property
    def header_1(self):
        text = i18n.t('main.main_info.header_1')
        return self.new_locator(
            desktop_xpath=f'//h1[.="{text}"]',
            description=f'Header "{text}"'
        )
