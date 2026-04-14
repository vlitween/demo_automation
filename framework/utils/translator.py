import os

import i18n


class Translator:
    def __init__(self, device):
        self.device = device

    @staticmethod
    def init_i18n(config):
        supported_locale = ['en', 'pt-br', 'zh-cn', 'ja']
        i18n.set('skip_locale_root', True)
        for locale in supported_locale:
            locales_dir = os.path.join('resources', 'locales', locale)
            i18n.load_path.append(locales_dir)

        if config.locale:
            current_locale = f'{config.locale}'.lower()
            if current_locale in supported_locale:
                i18n.set('locale', current_locale)
                return
            raise ValueError(f'Unsupported locale has set: {current_locale}')
        raise ValueError('Locale has not set. Please check your configuration.')

    def get_translation(self, translation_id):
        result = i18n.t(translation_id)
        if self.device.locale != 'en' and result == translation_id:
            result = i18n.t(translation_id, locale='en')
        if result != translation_id:
            return result
        else:
            raise AssertionError(f'Translation not found for id "{translation_id}"')

    @staticmethod
    def get_language_by_locale(locale: str):
        language_map = {
            'en': 'English',
            'pt-br': 'Português (Brasileiro)',
            'zh-cn': '中文简体',
            'ja': '日本語'
        }
        assert locale in language_map.keys(), f'Unsupported locale {locale}'
        return language_map[locale]

    def set_locale(self, locale: str):
        self.device.locale = locale
        i18n.set('locale', locale)

    def set_default_locale(self):
        if self.device.locale != 'en':
            self.set_locale('en')
