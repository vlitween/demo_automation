from playwright.sync_api import sync_playwright
from python_json_config import Config


class PlaywrightDevice:
    def __init__(self, config: Config):
        self.playwright = sync_playwright().start()
        if config.playwright.use_local:
            self.browser = self.playwright.chromium.launch(
                args=['--start-maximized'],
                headless=config.playwright.headless
            )
        else:
            self.browser = self.playwright.chromium.connect(config.playwright.remote_ws_address)
        if config.playwright.headless or not config.playwright.use_local:
            self.context = self.browser.new_context(viewport={'width': 1920, 'height': 1080})
        else:
            self.context = self.browser.new_context(no_viewport=True)
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
