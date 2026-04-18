from framework.driver.android_device import AndroidDevice
from framework.page_object.base.actions.selenium_actions import SeleniumActions


class AndroidActions(SeleniumActions):
    def __init__(self, device: AndroidDevice):
        super().__init__(device)
        self.device = device
