import time
from typing import Union

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.driver.selenium_device import SeleniumDevice
from framework.page_object.base.base_locator import UniversalLocator
from framework.utils.image_processor import ImageProcessor


class SeleniumActions:
    def __init__(self, device: SeleniumDevice):
        self.device = device

    def open_url(self, url):
        return self.device.driver.get(url)

    def get_page_url(self):
        actual_url = self.device.driver.current_url
        return actual_url

    def wait_page_title(self, expected_title, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            actual_title = self.device.driver.title
            if actual_title == expected_title:
                return
            time.sleep(1)
        raise AssertionError(f'Page title "{expected_title}" not found after {timeout} seconds')

    def find_element(self, locator: UniversalLocator, no_wait=False, timeout=10, should_be_visible=False) -> Union[WebElement, None]:
        xpath = locator.chrome_xpath
        try:
            if no_wait:
                return self.device.driver.find_element(By.XPATH, xpath)
            else:
                wait = WebDriverWait(self.device.driver, timeout)
                if should_be_visible:
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
                else:
                    return wait.until(
                        expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except (TimeoutException, NoSuchElementException):
            return None

    def find_sub_element(self, element: WebElement, locator: UniversalLocator, no_wait=False, timeout=10) -> Union[WebElement, None]:
        xpath = f'.{locator.chrome_xpath}' if not locator.chrome_xpath.startswith('.') else locator.chrome_xpath
        try:
            if no_wait:
                return element.find_element(By.XPATH, xpath)
            else:
                start_time = time.time()
                while time.time() - start_time < timeout:
                    try:
                        return element.find_element(By.XPATH, xpath)
                    except NoSuchElementException:
                        time.sleep(0.5)
                raise NoSuchElementException
        except NoSuchElementException:
            return None

    def find_elements(self, locator: UniversalLocator, no_wait=False, timeout=10) -> Union[list[WebElement], None]:
        xpath = locator.chrome_xpath
        try:
            if no_wait:
                return self.device.driver.find_elements(By.XPATH, xpath)
            else:
                return WebDriverWait(self.device.driver, timeout).until(
                    expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        except (TimeoutException, NoSuchElementException):
            return None

    def check_item_exists(self, locator: UniversalLocator, parent_element: WebElement = None, no_wait=False, timeout=10, should_be_visible=False):
        if parent_element:
            item = self.find_sub_element(parent_element, locator, no_wait, timeout)
        else:
            item = self.find_element(locator, no_wait, timeout, should_be_visible)
        assert item, f'Item not found: {locator.description}'
        return item

    def scroll_to_element(self, element: WebElement, to_top: bool = True, offset: int = 100):
        """
        Scrolls to an element with an optional pixel offset.
        :param element: The WebElement to scroll to.
        :param to_top: If True, aligns to top. If False, aligns to bottom.
        :param offset: Pixels to adjust the final position.
        """
        if offset is None:
            # Standard behavior
            alignment = 'true' if to_top else 'false'
            self.device.driver.execute_script(f"arguments[0].scrollIntoView({alignment});", element)
        else:
            # Manual calculation with offset
            if to_top:
                # element top - offset (moves the element further down from the top)
                script = """
                var elementRect = arguments[0].getBoundingClientRect();
                var absoluteElementTop = elementRect.top + window.pageYOffset;
                window.scrollTo({
                    top: absoluteElementTop - arguments[1],
                    behavior: 'smooth'
                });
                """
            else:
                # element bottom + offset - viewport height (aligns bottom with a gap)
                script = """
                var elementRect = arguments[0].getBoundingClientRect();
                var absoluteElementBottom = elementRect.bottom + window.pageYOffset;
                var viewportHeight = window.innerHeight;
                window.scrollTo({
                    top: absoluteElementBottom + arguments[1] - viewportHeight,
                    behavior: 'smooth'
                });
                """
            self.device.driver.execute_script(script, element, offset)

        time.sleep(0.5)

    def click_element(self, locator: UniversalLocator, parent_element=None, no_wait=False, timeout=10, should_be_visible=False):
        if parent_element:
            element = self.find_sub_element(parent_element, locator, no_wait, timeout)
        else:
            element = self.find_element(locator, no_wait, timeout, should_be_visible)
        if not should_be_visible:
            self.scroll_to_element(element)
        element.click()

    def get_element_text(self, element: WebElement):
        text = element.text.replace('\n', ' ').strip()
        return text

    def get_element_attribute(self, element: WebElement, attribute: str):
        return element.get_attribute(attribute)

    def verify_image(self, actual_image: WebElement, expected_image_path: str, expected_threshold: int = 40):
        actual_image_bytes = actual_image.screenshot_as_png
        actual_threshold = ImageProcessor().get_image_similarity_index(actual_image_bytes, expected_image_path)
        assert actual_threshold <= expected_threshold, f'Image similarity threshold exceeded. Actual {actual_threshold}, expected {expected_threshold}'
