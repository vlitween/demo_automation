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
