import pytest

from framework.utils.translator import Translator

supported_locale = ['en', 'pt-br', 'zh-cn', 'ja']


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    Translator.init_i18n(config.cfg)
