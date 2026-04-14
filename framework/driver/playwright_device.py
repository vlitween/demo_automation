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

        self.config = config
        self.device_type = 'playwright'
        self.locale = config.locale

    def stop(self):
        try:
            if hasattr(self, 'page') and self.page:
                self.page.close()
        except Exception as e:
            print(f'Error on closing page: {e}')

        try:
            if hasattr(self, 'context') and self.context:
                self.context.close()
        except Exception as e:
            print(f'Error on closing context: {e}')

        try:
            if hasattr(self, 'browser') and self.browser:
                self.browser.close()
        except Exception as e:
            print(f'Error on closing browser: {e}')

        try:
            if hasattr(self, 'playwright') and self.playwright:
                self.playwright.stop()
        except Exception as e:
            print(f'Error on stopping Playwright: {e}')

    def get_screenshot(self):
        return self.page.screenshot()

    def get_page_source(self):
        return self.page.content()
