import logging

import allure
import pytest

from framework.driver.selenium_driver import SeleniumDriver

pytest_plugins = ['plugins.locale', 'plugins.config', 'plugins.allure']

logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        driver = item.funcargs['device']

        if report.failed:
            try:
                page_source = driver.page_source
                allure.attach(page_source, name='Page Source', attachment_type=allure.attachment_type.XML)
            except Exception as e:
                allure.attach(str(e), name='Page Source', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope='function')
def device(request, config):
    if request.param == 'desktop':
        engine = config.browser_engine
        if engine == 'selenium':
            caps = config.selenium.capabilities.to_dict()
            if config.selenium.use_local:
                driver = SeleniumDriver().driver_init(caps=caps)
            else:
                remote_ip = config.selenium.remote_driver_address
                driver = SeleniumDriver().driver_init(caps=caps, remote_ip=remote_ip)
            driver.config = config
            driver.device_type = 'selenium'
            yield driver
            driver.close()
