from flask import Blueprint, request
from app.controllers.sessions.activities.placement_controller import PlacementController
from app.controllers.routers.respondable import respondable

namespace = '/sessions/<session_token>/activities/<activity_token>/placement'
app = Blueprint('sessions_activities_placement', __name__)


@app.route(namespace, methods=['PUT'])
@respondable
def upsert(session_token, activity_token):
    params = request.get_json()
    params.update({'session_token': session_token, 'activity_token': activity_token})
    return PlacementController.upsert(params)
