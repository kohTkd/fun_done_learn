from flask import Flask
from app.controllers.routers import boards_router

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(boards_router.app)


@app.route('/boards/<board_token>/notes', methods=['POST'])
def create_note(board_token):
    pass


@app.route('/boards/<board_token>/sticky_notes', methods=['GET'])
def index_sticky_notes(board_token):
    pass


@app.route('/boards/<board_token>/sticky_notes', methods=['POST'])
def create_sticky_note(board_token):
    pass


@app.route('/boards/<board_token>/sticky_notes/<sticky_note_token>', methods=['PUT'])
def update_sticky_note(board_token, sticky_note_token):
    pass


@app.route('/boards/<board_token>/sticky_notes/<sticky_note_token>/comments', methods=['POST'])
def create_comment(board_token, sticky_note_token):
    pass


if __name__ == '__main__':
    app.run(port=5000)
