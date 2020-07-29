from app.entities.activity import Activity
from app.errors.invalid_parameters_error import InvalidParametersError
from app.errors.not_persisted_error import NotPersistedError
from app.forms.activity_form import ActivityForm
from app.services.placements_service import PlacementsService
from app.repositories.activities_repository import ActivitiesRepository


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
        return ActivitiesRepository().save(activity)

    @classmethod
    def find(cls, session_token, token) -> Activity:
        activity = ActivitiesRepository().find(session_token, token)
        if not activity:
            return activity
        activity.placement = PlacementsService.find_or_build(session_token, token)
        return activity

    @classmethod
    def query(cls, session_token):
        activities = sorted(ActivitiesRepository().query(session_token), key=lambda act: act.token)
        placements = sorted(PlacementsService.query(session_token), key=lambda plc: plc.activity_token)

        placements_count = len(placements)
        j = 0
        for i in range(len(activities)):
            if j < placements_count and activities[i].token == placements[j].activity_token:
                activities[i].placement = placements[j]
                j += 1
        return activities

    @classmethod
    def update(cls, activity, form):
        activity.update(content=form.content)
        return cls.save(activity)

    @classmethod
    def destroy(cls, activity: Activity):
        if not activity.is_persisted():
            raise NotPersistedError(
                Activity,
                session_token=activity.session_token,
                activity_token=activity.activity_token
            )

        ActivitiesRepository().destroy(activity)
