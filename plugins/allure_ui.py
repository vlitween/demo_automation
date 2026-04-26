import allure_commons
import pytest

from framework.allure import (allure_step_enter_wrapper_ui,
                              allure_step_exit_wrapper_ui)

orig_func_exit = allure_commons._allure.StepContext.__exit__
orig_func_enter = allure_commons._allure.StepContext.__enter__


@pytest.fixture(autouse=True, scope='function')
def override_allure(device):
    allure_commons._allure.StepContext.__enter__ = allure_step_enter_wrapper_ui(device, orig_func_enter)
    allure_commons._allure.StepContext.__exit__ = allure_step_exit_wrapper_ui(device, orig_func_exit)
    yield
    allure_commons._allure.StepContext.__enter__ = orig_func_enter
    allure_commons._allure.StepContext.__exit__ = orig_func_exit
