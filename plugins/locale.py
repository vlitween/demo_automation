import os

import i18n
import pytest

supported_locale = ['en', 'ch']


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    i18n.set('skip_locale_root', True)
    for locale in supported_locale:
        locales_dir = os.path.join(config.rootdir.strpath, 'resources', 'locales', locale)
        i18n.load_path.append(locales_dir)

    if config.cfg.locale:
        current_locale = f'{config.cfg.locale}'.lower()
        if current_locale in supported_locale:
            i18n.set('locale', current_locale)
            return
        raise ValueError(f'Unsupported locale has set: {current_locale}')
    raise ValueError('Locale has not set. Please check your configuration.')
