from abc import ABCMeta, abstractmethod
import os
import yaml


class ApplicationError(Exception, metaclass=ABCMeta):
    def __init__(self, model, **kwargs):
        super().__init__()
        self.model = model
        self._options = kwargs

    @abstractmethod
    def error_messages(self):
        raise NotImplementedError()

    def _translated_model(self):
        with open(f"{self._locale_path()}/{self.model().model_name}.yml", 'r') as yml:
            locale = yaml.load(yml, Loader=yaml.FullLoader)

        return locale['model']

    def _locale_path(self):
        return f"{os.path.dirname(__file__)}/../../config/locale/ja"
