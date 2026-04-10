import i18n


class Translator:
    def __init__(self, device):
        self.device = device

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
