class InvalidEntityError(Exception):
    def __init__(self, model):
        self.model = model

    def error_messages(self):
        return self.model.error_messages()
