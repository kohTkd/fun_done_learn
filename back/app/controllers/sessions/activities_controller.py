from app.errors.invalid_entity_error import InvalidEntityError
from app.errors.not_found_error import NotFoundError
from app.forms.activity_form import ActivityForm
from app.use_cases.create_activity_use_case import CreateActivityUseCase
from app.use_cases.find_activities_use_case import FindActivitiesUseCase
from app.presenters.activity_presenter import ActivityPresenter
from app.lib.api_response import ApiResponse


class ActivitiesController():
    @classmethod
    def create(cls, params: dict) -> ApiResponse:
        form = ActivityForm(**params)
        if form.is_invalid():
            return ApiResponse.unprocessable_entity(form.error_messages())
        try:
            activity = CreateActivityUseCase.execute(form)
            return ApiResponse.created(cls._detail(activity))
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())
        except InvalidEntityError as e:
            return ApiResponse.unprocessable_entity(e.error_messages())

    @classmethod
    def index(cls, params: dict) -> ApiResponse:
        try:
            activities = FindActivitiesUseCase.execute(params.get('session_token'))
            return ApiResponse.ok(cls._details(activities))
        except NotFoundError as e:
            return ApiResponse.not_found(e.error_messages())

    @classmethod
    def _detail(cls, activity) -> dict:
        return ActivityPresenter(activity).detail()

    @classmethod
    def _details(cls, activities) -> list:
        return [cls._detail(activity) for activity in activities]

    # @classmethod
    # def show(cls, params: dict) -> ApiResponse:
    #     try:
    #         session = FindSessionUseCase.execute(params.get('token'))
    #         return ApiResponse.ok(cls._detail(session))
    #     except NotFoundError as e:
    #         return ApiResponse.not_found(e.error_messages())
