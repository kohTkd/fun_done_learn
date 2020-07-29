from app.entities.placement import Placement
from app.errors.not_persisted_error import NotPersistedError
from app.repositories.placements_repository import PlacementsRepository


class PlacementsService():
    @classmethod
    def save(cls, placement: Placement) -> Placement:
        PlacementsRepository().save(placement)
        return placement

    @classmethod
    def find(cls, session_token, activity_token) -> Placement:
        return PlacementsRepository().find(session_token, activity_token)

    @classmethod
    def find_or_build(cls, session_token, activity_token) -> Placement:
        placement = PlacementsRepository().find(session_token, activity_token)
        if placement:
            return placement
        return Placement(session_token=session_token, activity_token=activity_token)

    @classmethod
    def destroy(cls, placement: Placement):
        if not placement.is_persisted():
            raise NotPersistedError(
                Placement,
                session_token=placement.session_token,
                activity_token=placement.activity_token
            )

        return PlacementsRepository().destroy(placement)

    @classmethod
    def query(cls, session_token):
        return PlacementsRepository().query(session_token)
