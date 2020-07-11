from flask import Blueprint, request
from app.controllers.sessions.sticky_notes_controller import StickyNotesController
from app.lib.mixin.respondable import respondable

namespace = '/sessions/<session_token>/sticky_notes'
app = Blueprint('sessions_sticky_notes', __name__)


@app.route(namespace, methods=['POST'])
@respondable
def create(session_token):
    params = request.get_json()
    params.update({'session_token': session_token})
    return StickyNotesController.create(params)
