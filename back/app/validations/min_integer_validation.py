from app.validations.validation import Validation, validation_method


class MinIntegerValidation(Validation):
    def __init__(self, model, attr_name, **kwargs):
        super().__init__(model, attr_name)
        self._limit = kwargs['limit']

    @validation_method
    def _execute(self):
        self._valid = (not self._value()) or not isinstance(self._value(), int) or self._value() >= self._limit
        return self._valid

    def message(self):
        return f"{self._translated_attr()}は{self._limit}以上で設定してください"
