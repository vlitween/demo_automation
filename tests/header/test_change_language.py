import allure
import pytest


class TestChangeLanguage:
    @allure.title('Test change language')
    @pytest.mark.parametrize('device', ['chrome'], indirect=True)
    def test_positive(self, device, page):
        actual_locale = device.locale
        locales_sequence = ['en', 'pt-br', 'zh-cn', 'ja']
        locales_sequence.remove(actual_locale)
        locales_sequence.append(actual_locale)
        main_page = page.main_page
        documentation_page = page.documentation_page

        with allure.step('Open Main page'):
            main_page.open_page()
        with allure.step('Check Main page has opened'):
            main_page.check_page_presence(fast_check=True)
        for target_locale in locales_sequence:
            with allure.step('Click language button'):
                main_page.header.click_language_button()
            with allure.step('Check language selection dropdown'):
                main_page.header.check_presence_language_selection_dropdown()
            target_language = main_page.translator.get_language_by_locale(target_locale)
            with allure.step(f'Change language to {target_language}'):
                main_page.header.select_language(target_language)
            with allure.step(f'Change device locale to {target_locale}'):
                main_page.translator.set_locale(target_locale)
            with allure.step('Check Main page is displayed according to selected language'):
                main_page.check_page_presence()
            with allure.step('Navigate to the Documentation page'):
                main_page.header.click_documentation_button()
            with allure.step('Check Documentation page is displayed according to selected language'):
                assert device.locale == target_locale  # Ensure device locale is correct
                documentation_page.check_page_presence(fast_check=True)
            with allure.step('Go back to the Main page'):
                documentation_page.header.click_logo()
            with allure.step('Check Main page is still displayed according to selected language'):
                assert device.locale == target_locale  # Ensure device locale is correct
                main_page.check_page_presence()
