from flask import Blueprint, request
from app.controllers.sessions.activities_controller import ActivitiesController
from app.controllers.decorators.routers.respondable import respondable

namespace = '/sessions/<session_token>/activities'
app = Blueprint('sessions_activities', __name__)


@app.route(namespace, methods=['POST'])
@respondable
def create(session_token):
    params = request.get_json()
    params.update({'session_token': session_token})
    return ActivitiesController.create(params)


@app.route(namespace, methods=['GET'])
@respondable
def index(session_token):
    return ActivitiesController.index({'session_token': session_token})


@app.route(f"{namespace}/<token>", methods=['PATCH'])
@respondable
def update(session_token, token):
    params = request.get_json()
    params.update({'session_token': session_token, 'token': token})
    return ActivitiesController.update(params)


@app.route(f"{namespace}/<token>", methods=['DELETE'])
@respondable
def destroy(session_token, token):
    return ActivitiesController.destroy({'session_token': session_token, 'token': token})
