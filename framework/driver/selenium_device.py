from python_json_config import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumDevice:
    def __init__(self, config: Config):
        self.config = config
        self.__driver = None

    @property
    def driver(self) -> WebDriver:
        if not self.__driver:
            chrome_options = Options()
            if self.config.selenium.capabilities:
                for key, value in self.config.selenium.capabilities.to_dict().items():
                    if key == 'goog:chromeOptions' and 'args' in value:
                        for arg in value['args']:
                            chrome_options.add_argument(arg)
                    else:
                        chrome_options.set_capability(key, value)
            is_local = self.config.selenium.use_local if self.config.selenium.use_local is not None else True
            if not is_local:
                driver = webdriver.Remote(
                    command_executor=self.config.selenium.remote_driver_address,
                    options=chrome_options
                )
            else:
                driver = webdriver.Chrome(options=chrome_options)
            self.__driver = driver
            return driver
        else:
            return self.__driver

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()

    def get_page_source(self):
        return self.driver.page_source
