from app.entities.placement import Placement
from app.errors.not_found_error import NotFoundError
from app.repositories.placements_repository import PlacementsRepository


class PlacementsService():
    @classmethod
    def save(cls, placement):
        PlacementsRepository().save(placement)

    @classmethod
    def find(cls, session_token, activity_token) -> Placement:
        return PlacementsRepository().find(session_token, activity_token)

    @classmethod
    def find_or_build(cls, session_token, activity_token) -> Placement:
        try:
            return PlacementsRepository().find(session_token, activity_token)
        except NotFoundError:
            return Placement(session_token=session_token, activity_token=activity_token)

    @classmethod
    def query(cls, session_token):
        return PlacementsRepository().query(session_token)
