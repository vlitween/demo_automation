import allure
import pytest

import variables
from framework.page_object.pages.main import MainPage


class TestMain:
    @allure.title('Test main page')
    @pytest.mark.parametrize('device', ['desktop'], indirect=True)
    def test_positive(self, device):
        main_page = MainPage(device)
        with allure.step('Open site'):
            main_page.actions.open_url(variables.MAIN_URL)
        with allure.step('Check displaying main page'):
            main_page.check_main_page()
