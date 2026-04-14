import allure
import i18n
import pytest

from framework.driver.playwright_device import PlaywrightDevice
from framework.driver.selenium_device import SeleniumDevice
from framework.page_object.base.page_factory import Page

pytest_plugins = ['plugins.locale', 'plugins.config', 'plugins.allure']


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        device = item.funcargs['device']

        if report.failed:
            try:
                page_source = device.get_page_source()
                allure.attach(page_source, name='Page Source', attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), name='Page Source', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(autouse=True)
def reset_locale(config):
    initial_locale = i18n.get('locale')
    yield
    i18n.set('locale', initial_locale)


@pytest.fixture(scope='function')
def selenium(request, config):
    device = SeleniumDevice(config)
    device.config = config
    device.device_type = 'selenium'
    device.locale = config.locale
    if config.selenium.window_size:
        device.driver.set_window_size(*config.selenium.window_size)
    else:
        device.driver.maximize_window()
    yield device
    device.driver.quit()


@pytest.fixture(scope='function')
def playwright(request, config):
    playwright_device = PlaywrightDevice(config)
    yield playwright_device
    playwright_device.stop()


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
