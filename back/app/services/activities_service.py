from app.entities.activity import Activity
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.activity_form import ActivityForm
from app.repositories.activities_repository import ActivitiesRepository
from app.repositories.placements_repository import PlacementsRepository


class ActivitiesService():
    @classmethod
    def generate(cls, form: ActivityForm) -> Activity:
        if form.is_invalid():
            raise InvalidParametersError(form)
        activity = Activity(content=form.content, session_token=form.session_token)
        activity.generate_token()
        return activity

    @classmethod
    def save(cls, activity):
        ActivitiesRepository().save(activity)

    @classmethod
    def find(cls, session_token, token) -> Activity:
        return ActivitiesRepository().find(session_token, token)

    @classmethod
    def query(cls, session_token):
        activities = ActivitiesRepository().query(session_token)
        placements = PlacementsRepository().query(session_token)

        for placement in placements:
            activity = cls.__find_activity(activities, placement.activity_token)
            if activity:
                activity.placement = placement
        return activities

    @classmethod
    def __find_activity(cls, activities, token):
        match_activities = [activity for activity in activities if activity.token == token]
        return match_activities[0] if match_activities else None
