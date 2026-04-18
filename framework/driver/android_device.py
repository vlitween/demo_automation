from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver
from python_json_config import Config


class AndroidDevice:
    def __init__(self, config: Config, worker_id: str):
        self.config = config
        self.worker_id = worker_id
        self.__driver = None

    @property
    def driver(self) -> WebDriver:
        if not self.__driver:
            options = self.options_configurator(self.config, self.worker_id)
            endpoint = self.config.android.appium_endpoint
            appium_driver = webdriver.Remote(endpoint, options=options)
            self.__driver = appium_driver
            return appium_driver
        else:
            return self.__driver

    @staticmethod
    def options_configurator(config, worker_id):
        device_pool = config.android.device_pool
        if worker_id == 'master':
            device_config = device_pool[0]
        else:
            index = int(worker_id.replace('gw', ''))
            device_config = device_pool[index]
        options = UiAutomator2Options()
        options.load_capabilities(config.android.capabilities.to_dict())
        options.auto_accept_alerts = True
        options.auto_grant_permissions = True
        options.load_capabilities(device_config)
        options.udid = device_config['udid']
        options.system_port = device_config['sys_port']
        options.chromedriver_port = device_config['chrome_port']
        return options

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()

    def get_page_source(self):
        return self.driver.page_source

    def set_context_native(self):
        self.driver.switch_to.context('NATIVE_APP')
