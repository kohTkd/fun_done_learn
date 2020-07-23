from flask import Blueprint, request
from app.controllers.sessions.notes_controller import NotesController
from app.controllers.routers.respondable import respondable

namespace = '/sessions/<session_token>/notes'
app = Blueprint('sessions_notes', __name__)


@app.route(namespace, methods=['POST'])
@respondable
def create(session_token):
    params = request.get_json()
    params.update({'session_token': session_token})
    return NotesController.create(params)


@app.route(namespace, methods=['GET'])
@respondable
def index(session_token):
    return NotesController.index({'session_token': session_token})
