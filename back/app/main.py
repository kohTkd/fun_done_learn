from flask import Flask
from flask_cors import CORS
from app.controllers.routers import sessions_router
from app.controllers.routers.sessions import sticky_notes_router

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(sessions_router.app)
app.register_blueprint(sticky_notes_router.app)


@app.route('/sessions/<session_token>/notes', methods=['POST'])
def create_note(session_token):
    pass


@app.route('/sessions/<session_token>/sticky_notes', methods=['GET'])
def index_sticky_notes(session_token):
    pass


@app.route('/sessions/<session_token>/sticky_notes', methods=['POST'])
def create_sticky_note(session_token):
    pass


@app.route('/sessions/<session_token>/sticky_notes/<sticky_note_token>', methods=['PUT'])
def update_sticky_note(session_token, sticky_note_token):
    pass


@app.route('/sessions/<session_token>/sticky_notes/<sticky_note_token>/comments', methods=['POST'])
def create_comment(session_token, sticky_note_token):
    pass


if __name__ == '__main__':
    app.run(port=5000)
