from app.entities.session import Session
from app.entities.activity import Activity
from app.errors.not_found_error import NotFoundError
from app.forms.activity_form import ActivityForm
from app.services.sessions_service import SessionsService
from app.services.activities_service import ActivitiesService


class UpdateActivityUseCase():
    @classmethod
    def execute(cls, form: ActivityForm) -> Activity:
        session = SessionsService.find(form.session_token)
        if not session:
            raise NotFoundError(Session, token=form.session_token)

        activity = ActivitiesService.find(form.session_token, form.token)
        if not activity:
            raise NotFoundError(Activity, token=form.token)

        ActivitiesService.update(activity, form)

        return activity
