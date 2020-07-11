from flask import Blueprint, request
from app.controllers.sessions_controller import SessionsController
from app.lib.mixin.respondable import respondable

namespace = '/sessions'
app = Blueprint('sessions', __name__)


@app.route(namespace, methods=['POST'])
@respondable
def create():
    return SessionsController.create(request.get_json())


@app.route(f"{namespace}/<token>", methods=['GET'])
@respondable
def show(token):
    return SessionsController.show({'token': token})
