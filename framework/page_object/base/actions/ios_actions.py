from framework.driver.ios_device import IOSDevice
from framework.page_object.base.actions.selenium_actions import SeleniumActions


class IOSActions(SeleniumActions):
    def __init__(self, device: IOSDevice):
        super().__init__(device)
        self.device = device
