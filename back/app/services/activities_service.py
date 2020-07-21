from app.entities.activity import Activity
from app.errors.invalid_parameters_error import InvalidParametersError
from app.forms.activity_form import ActivityForm
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
        ActivitiesRepository().save(activity)

    @classmethod
    def find(cls, session_token, token) -> Activity:
        return ActivitiesRepository().find(session_token, token)

    @classmethod
    def query(cls, session_token):
        return ActivitiesRepository().query(session_token)
