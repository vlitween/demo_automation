from playwright.sync_api import sync_playwright
from python_json_config import Config


class PlaywrightDevice:
    def __init__(self, config: Config):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            args=['--start-maximized'],
            headless=config.playwright.headless
        )
        self.context = self.browser.new_context(no_viewport=True) if not config.playwright.headless\
            else self.browser.new_context(viewport={'width': int(config.playwright.headless_window_size[0]), 'height': int(config.playwright.headless_window_size[1])})
        self.page = self.context.new_page()

    def stop(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def get_screenshot(self):
        return self.page.screenshot()

    def get_page_source(self):
        return self.page.content()
