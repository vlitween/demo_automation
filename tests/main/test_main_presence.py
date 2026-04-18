import allure
import pytest


class TestMainPresence:
    @allure.title('Test main page')
    @pytest.mark.smoke
    @pytest.mark.parametrize('device', ['chrome', 'android', 'ios'], indirect=True)
    def test_positive(self, device, page):
        main_page = page.main_page
        with allure.step('Open Main page'):
            main_page.open_page()
        with allure.step('Check Main page'):
            main_page.check_page_presence()
