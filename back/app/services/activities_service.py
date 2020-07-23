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
        activities = sorted(ActivitiesRepository().query(session_token), key=lambda act: act.token)
        placements = sorted(PlacementsRepository().query(session_token), key=lambda plc: plc.activity_token)

        placements_count = len(placements)
        j = 0
        for i in range(len(activities)):
            if j < placements_count and activities[i].token == placements[j].activity_token:
                activities[i].placement = placements[j]
                j += 1
        return activities
