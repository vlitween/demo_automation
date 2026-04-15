from playwright.sync_api import sync_playwright
from python_json_config import Config


class PlaywrightDevice:
    def __init__(self, config: Config):
        is_local = config.playwright.use_local if config.playwright.use_local is not None else True
        is_headless = config.playwright.headless if config.playwright.headless is not None else False
        self.playwright = sync_playwright().start()

        if is_local:
            self.browser = self.playwright.chromium.launch(
                args=['--start-maximized'],
                headless=is_headless
            )
        else:
            remote_address = config.playwright.remote_ws_address if config.playwright.remote_ws_address is not None else 'ws://localhost:8080/'
            self.browser = self.playwright.chromium.connect(remote_address)
        if is_headless or not is_local:
            size = config.playwright.window_size if config.playwright.window_size is not None else [1920, 1080]
            self.context = self.browser.new_context(viewport={'width': size[0], 'height': size[1]})
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
