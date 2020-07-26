import functools

from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.invalid_parameters_error import InvalidParametersError
from app.errors.not_found_error import NotFoundError
from app.lib.api_response import ApiResponse

from app.use_cases.bloadcast_use_case import BloadcastUseCase


def error_handleable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> ApiResponse:
        try:
            return func(*args, **kwargs)
        except (InvalidParametersError, InvalidEntityError) as e:
            return ApiResponse.unprocessable_entity(e.error_messages())
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())
    return wrapper


def bloadcastable(resource_name: str, action: str):
    def _bloadcastable(func):
        def wrapper(*args, **kwargs) -> ApiResponse:
            response = func(*args, **kwargs)
            if response.succeeded():
                BloadcastUseCase.execute(response.body, resource_name, action)
            return response
        return wrapper
    return _bloadcastable
