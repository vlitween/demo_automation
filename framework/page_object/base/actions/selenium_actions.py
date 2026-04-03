import time
from typing import Union

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.page_object.base.base_locator import UniversalLocator


class SeleniumActions:
    def __init__(self, device: WebDriver):
        self.device = device

    def open_url(self, url):
        return self.device.get(url)

    def wait_page_title(self, expected_title, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            actual_title = self.device.title
            if actual_title == expected_title:
                return
            time.sleep(1)
        raise TimeoutException(f'Page title "{expected_title}" not found after {timeout} seconds')

    def find_element(self, locator: UniversalLocator, no_wait=False, timeout=10, should_be_visible=False) -> Union[WebElement, None]:
        xpath = locator.desktop_xpath
        try:
            if no_wait:
                return self.device.find_element(By.XPATH, xpath)
            else:
                wait = WebDriverWait(self.device, timeout)
                if should_be_visible:
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
                else:
                    return wait.until(
                        expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except (TimeoutException, NoSuchElementException):
            return None

    def check_item_exists(self, locator: UniversalLocator, no_wait=False, timeout=10, should_be_visible=False):
        item = self.find_element(locator, no_wait, timeout, should_be_visible)
        assert item, f'Item not found: {locator.description}'

    def click_element(self, locator: UniversalLocator, no_wait=False, timeout=10, should_be_visible=False):
        element = self.find_element(locator, no_wait, timeout, should_be_visible)
        element.click()
