from app.entities.session import Session
from app.entities.activity import Activity
from app.entities.placement import Placement
from app.errors.not_found_error import NotFoundError
from app.forms.placement_form import PlacementForm
from app.services.sessions_service import SessionsService
from app.services.activities_service import ActivitiesService
from app.services.placements_service import PlacementsService


class UpsertPlacementUseCase():
    @classmethod
    def execute(cls, form: PlacementForm) -> Placement:
        session = SessionsService.find(form.session_token)
        if not session:
            raise NotFoundError(Session, token=form.session_token)

        activity = ActivitiesService.find(form.session_token, form.activity_token)
        if not activity:
            raise NotFoundError(Activity, token=form.activity_token)

        placement = PlacementsService.find_or_generate(form.session_token, form.activity_token, form)
        if placement:
            placement.update(left=form.left, top=form.top)
        else:
            placement = PlacementsService.generate(form)
        PlacementsService.save(placement)
        return placement
