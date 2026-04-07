import allure
import pytest


class TestMain:
    @allure.title('Test main page')
    @pytest.mark.parametrize('device', ['chrome'], indirect=True)
    def test_positive(self, device, page):
        main_page = page.main_page
        with allure.step('Open site'):
            main_page.actions.open_url(main_page.url)
        with allure.step('Check Main page'):
            main_page.check_main_page()
