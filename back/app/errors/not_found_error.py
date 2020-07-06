import os
import yaml


class NotFoundError(Exception):
    def __init__(self, clazz, **kwargs):
        self._clazz = clazz
        self._options = kwargs

    def error_messages(self):
        return f"{self._translated_model()}が見つかりません"

    def _translated_model(self):
        with open(f"{self._locale_path()}/{self._clazz().model_name}.yml", 'r') as yml:
            locale = yaml.load(yml, Loader=yaml.FullLoader)

        return locale['model']

    def _locale_path(self):
        return f"{os.path.dirname(__file__)}/../../config/locale/ja"
