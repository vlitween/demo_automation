import allure
import pytest

import variables


class TestMain:
    @allure.title('Test main page')
    @pytest.mark.parametrize('device', ['chrome'], indirect=True)
    def test_positive(self, device, page):
        main_page = page.main_page
        with allure.step('Open site'):
            main_page.actions.open_url(variables.MAIN_URL)
        with allure.step('Check main page'):
            main_page.check_main_page()
