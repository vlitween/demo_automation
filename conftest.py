import allure
import pytest

from framework.driver.selenium_driver import SeleniumDriver
from framework.page_object.base.page_factory import Page

pytest_plugins = ['plugins.locale', 'plugins.config', 'plugins.allure']


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        driver = item.funcargs['device']

        if report.failed:
            try:
                page_source = driver.page_source
                allure.attach(page_source, name='Page Source', attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), name='Page Source', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope='function')
def selenium(request, config):
    caps = config.selenium.capabilities.to_dict()
    if config.selenium.use_local:
        remote_ip = None
    else:
        remote_ip = config.selenium.remote_driver_address
    driver = SeleniumDriver().driver_init(caps=caps, remote_ip=remote_ip)
    driver.config = config
    driver.device_type = 'selenium'
    driver.locale = config.locale
    if config.selenium.window_size:
        driver.set_window_size(*config.selenium.window_size)
    else:
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def device(request, config):
    if request.param == 'chrome':
        device_name = config.browser_engine
    else:
        device_name = request.param
    return request.getfixturevalue(device_name)


@pytest.fixture(scope='function')
def page(device):
    return Page(device)
