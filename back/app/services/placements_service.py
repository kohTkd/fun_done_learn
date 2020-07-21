from app.entities.placement import Placement
from app.errors.invalid_parameters_error import InvalidParametersError
from app.errors.not_found_error import NotFoundError
from app.forms.placement_form import PlacementForm
from app.repositories.placements_repository import PlacementsRepository


class PlacementsService():
    @classmethod
    def generate(cls, form: PlacementForm) -> Placement:
        if form.is_invalid():
            raise InvalidParametersError(form)
        return Placement(
            session_token=form.session_token, activity_token=form.activity_token,
            left=form.left, top=form.top
        )

    @classmethod
    def save(cls, placement):
        PlacementsRepository().save(placement)

    @classmethod
    def find(cls, session_token, activity_token) -> Placement:
        return PlacementsRepository().find(session_token, activity_token)

    @classmethod
    def find_or_generate(cls, session_token, activity_token, form: PlacementForm) -> Placement:
        try:
            return PlacementsRepository().find(session_token, activity_token)
        except NotFoundError:
            return cls.generate(form)

    @classmethod
    def query(cls, session_token):
        return PlacementsRepository().query(session_token)
