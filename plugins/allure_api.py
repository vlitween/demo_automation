import allure_commons
import pytest

from framework.allure import allure_step_enter_wrapper_api

orig_func_enter = allure_commons._allure.StepContext.__enter__


@pytest.fixture(autouse=True, scope='function')
def override_allure(config):
    allure_commons._allure.StepContext.__enter__ = allure_step_enter_wrapper_api(config, orig_func_enter)
    yield
    allure_commons._allure.StepContext.__enter__ = orig_func_enter
