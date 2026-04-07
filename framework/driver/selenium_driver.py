from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumDriver:
    def driver_init(self, caps=None, remote_ip=None):
        chrome_options = Options()
        if caps:
            for key, value in caps.items():
                if key == 'goog:chromeOptions' and 'args' in value:
                    for arg in value['args']:
                        chrome_options.add_argument(arg)
                else:
                    chrome_options.set_capability(key, value)
        if remote_ip:
            driver = webdriver.Remote(
                command_executor=remote_ip,
                options=chrome_options
            )
        else:
            driver = webdriver.Chrome(options=chrome_options)
        return driver
