from flask import Blueprint, request
from app.controllers.boards_controller import BoardsController
from app.lib.mixin.respondable import respondable

app = Blueprint('boards', __name__)


@app.route('/boards', methods=['POST'])
@respondable
def create_board():
    return BoardsController.create(request.get_json())


@app.route('/boards/<token>', methods=['GET'])
def show_board(token):
    pass
