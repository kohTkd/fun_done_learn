from app.errors.application_error import ApplicationError


class InvalidParametersError(ApplicationError):
    def error_messages(self):
        return self.model.error_messages()
