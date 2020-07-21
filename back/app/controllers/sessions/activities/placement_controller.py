from app.controllers.controller_method import controller_method
from app.forms.placement_form import PlacementForm
from app.use_cases.upsert_placement_use_case import UpsertPlacementUseCase
from app.presenters.placement_presenter import PlacementPresenter
from app.lib.api_response import ApiResponse


class PlacementController():
    @classmethod
    @controller_method
    def upsert(cls, params: dict) -> ApiResponse:
        form = PlacementForm(**params)
        placement = UpsertPlacementUseCase.execute(form)
        return ApiResponse.ok(cls._detail(placement))

    @classmethod
    def _detail(cls, placement) -> dict:
        return PlacementPresenter(placement).detail()
