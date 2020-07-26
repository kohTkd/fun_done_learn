from app.controllers.decorators.controller_methods import error_handleable
from app.forms.placement_form import PlacementForm
from app.use_cases.upsert_placement_use_case import UpsertPlacementUseCase
from app.presenters.placement_presenter import PlacementPresenter
from app.lib.api_response import ApiResponse


class PlacementController():
    @classmethod
    @error_handleable
    def upsert(cls, params: dict) -> ApiResponse:
        form = PlacementForm(**params)
        placement = UpsertPlacementUseCase.execute(form)
        return ApiResponse.ok(cls._detail(placement))

    @classmethod
    def _detail(cls, placement) -> dict:
        return PlacementPresenter(placement).detail()
