from python_json_config import ConfigBuilder

from framework.driver.playwright_device import PlaywrightDevice
from framework.page_object.base.page_factory import Page
from framework.utils.translator import Translator


def before_all(context):
    pass


def before_scenario(context, scenario):
    context.test_config = ConfigBuilder().parse_config('config/main.json')
    Translator.init_i18n(context.test_config)
    context.device = PlaywrightDevice(context.test_config)
    context.page = Page(context.device)


def after_scenario(context, scenario):
    try:
        context.device.stop()
    except Exception as e:
        print(e)


def after_all(context):
    pass
