from framework.page_object.base.actions.selenium_actions import SeleniumActions


def get_actions(device):
    device_type = device.device_type
    if device_type == 'selenium':
        return SeleniumActions(device)
    else:
        return None


class BasePage:
    def __init__(self, device):
        self.device = device
        self.actions = get_actions(device)
