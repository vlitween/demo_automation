import time
from typing import Union

from playwright.sync_api import Locator

from framework.driver.playwright_device import PlaywrightDevice
from framework.page_object.base.base_locator import UniversalLocator
from framework.utils.image_processor import ImageProcessor


class PlaywrightActions:
    def __init__(self, device: PlaywrightDevice):
        self.device = device

    def open_url(self, url):
        return self.device.page.goto(url)

    def get_page_url(self):
        actual_url = self.device.page.url
        return actual_url

    def wait_page_title(self, expected_title, timeout=10):
        start_time = time.time()
        actual_title = None
        while time.time() - start_time < timeout:
            actual_title = self.device.page.title()
            if actual_title == expected_title:
                return
            time.sleep(1)
        raise AssertionError(f'Page title "{expected_title}" not found after {timeout} seconds. Actual title is "{actual_title}"')

    def find_element(self, locator: UniversalLocator, no_wait=False, timeout=10, should_be_visible=False) -> Union[Locator, None]:
        xpath = f"xpath={locator.chrome_xpath}"
        element = self.device.page.locator(xpath).first
        try:
            if no_wait:
                if element.count() > 0:
                    return element
                return None
            else:
                timeout_ms = timeout * 1000
                if should_be_visible:
                    element.wait_for(state='visible', timeout=timeout_ms)
                else:
                    element.wait_for(state='attached', timeout=timeout_ms)
                return element
        except Exception as e:
            print(e)
            return None

    def find_sub_element(self, element: Locator, locator: UniversalLocator, no_wait=False, timeout=10) -> Union[Locator, None]:
        xpath = locator.chrome_xpath
        if not xpath.startswith('.'):
            xpath = f".{xpath}"

        sub_element = element.locator(f"xpath={xpath}").first

        try:
            if no_wait:
                if sub_element.count() > 0:
                    return sub_element
                return None
            else:
                sub_element.wait_for(state='attached', timeout=timeout * 1000)
                return sub_element
        except Exception as e:
            print(e)
            return None

    def find_elements(self, locator: UniversalLocator, no_wait=False, timeout=10) -> Union[list[Locator], None]:
        xpath = f"xpath={locator.chrome_xpath}"

        elements_collection = self.device.page.locator(xpath)

        try:
            if not no_wait:
                elements_collection.first.wait_for(state='attached', timeout=timeout * 1000)

            elements_list = elements_collection.all()

            return elements_list if len(elements_list) > 0 else None

        except Exception as e:
            print(e)
            return None

    def check_item_exists(self, locator: UniversalLocator, parent_element: Locator = None, no_wait=False, timeout=10, should_be_visible=False):
        if parent_element:
            item = self.find_sub_element(parent_element, locator, no_wait, timeout)
        else:
            item = self.find_element(locator, no_wait, timeout, should_be_visible)
        assert item, f'Item not found: {locator.description}'
        return item

    def scroll_to_element(self, element: Locator, to_top: bool = True, offset: int = 100):

        # Scrolls to an element with an optional pixel offset in Playwright.

        if offset is None:
            element.scroll_into_view_if_needed()
        else:
            if to_top:
                script = """
                (el, off) => {
                    const elementRect = el.getBoundingClientRect();
                    const absoluteElementTop = elementRect.top + window.pageYOffset;
                    window.scrollTo({
                        top: absoluteElementTop - off,
                        behavior: 'smooth'
                    });
                }
                """
            else:
                script = """
                (el, off) => {
                    const elementRect = el.getBoundingClientRect();
                    const absoluteElementBottom = elementRect.bottom + window.pageYOffset;
                    const viewportHeight = window.innerHeight;
                    window.scrollTo({
                        top: absoluteElementBottom + off - viewportHeight,
                        behavior: 'smooth'
                    });
                }
                """

            element.evaluate(script, offset)

        self.device.page.wait_for_load_state('networkidle')

    def click_element(self, locator: UniversalLocator, parent_element=None, no_wait=False, timeout=10, should_be_visible=False):
        if parent_element:
            element = self.find_sub_element(parent_element, locator, no_wait, timeout)
        else:
            element = self.find_element(locator, no_wait, timeout, should_be_visible)
        if not should_be_visible:
            self.scroll_to_element(element)
        element.click()

    def get_element_text(self, element: Locator):
        text = element.inner_text().replace('\n', ' ').strip()
        return text

    def get_element_attribute(self, element: Locator, attribute: str):
        return element.get_attribute(attribute)

    def verify_image(self, actual_image: Locator, expected_image_path: str, expected_threshold: int = 50):
        actual_image_bytes = actual_image.screenshot()
        actual_threshold = ImageProcessor().get_image_similarity_index(actual_image_bytes, expected_image_path)
        assert actual_threshold <= expected_threshold, f'Image similarity threshold exceeded. Actual {actual_threshold}, expected {expected_threshold}'
