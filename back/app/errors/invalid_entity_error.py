from app.errors.application_error import ApplicationError


class InvalidEntityError(ApplicationError):
    def error_messages(self):
        return self.model.error_messages()
