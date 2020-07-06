import os

from flask import Blueprint, request
from app.controllers.sessions_controller import SessionsController
from app.lib.mixin.respondable import respondable

app = Blueprint('sessions', __name__)


@app.route('/sessions', methods=['POST'])
@respondable
def create_session():
    return SessionsController.create(request.get_json())


@app.route('/sessions/<token>', methods=['GET'])
def show_session(token):
    pass