from app.controllers.decorators.controller_methods import error_handleable
from app.forms.activity_form import ActivityForm
from app.use_cases.create_activity_use_case import CreateActivityUseCase
from app.use_cases.find_activities_use_case import FindActivitiesUseCase
from app.presenters.activity_presenter import ActivityPresenter
from app.lib.api_response import ApiResponse


class ActivitiesController():
    @classmethod
    @error_handleable
    def create(cls, params: dict) -> ApiResponse:
        form = ActivityForm(**params)
        activity = CreateActivityUseCase.execute(form)
        return ApiResponse.created(cls._detail(activity))

    @classmethod
    @error_handleable
    def index(cls, params: dict) -> ApiResponse:
        activities = FindActivitiesUseCase.execute(params.get('session_token'))
        return ApiResponse.ok(cls._details(activities))

    @classmethod
    def _detail(cls, activity) -> dict:
        return ActivityPresenter(activity).detail()

    @classmethod
    def _details(cls, activities) -> list:
        return [cls._detail(activity) for activity in activities]
