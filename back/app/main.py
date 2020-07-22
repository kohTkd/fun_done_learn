from flask import Flask
from flask_cors import CORS
from app.controllers.routers import sessions_router
from app.controllers.routers.sessions import activities_router
from app.controllers.routers.sessions.activities import placement_router

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(sessions_router.app)
app.register_blueprint(activities_router.app)
app.register_blueprint(placement_router.app)


@app.route('/sessions/<session_token>/notes', methods=['POST'])
def create_note(session_token):
    pass


@app.route('/sessions/<session_token>/activities', methods=['GET'])
def index_activities(session_token):
    pass


@app.route('/sessions/<session_token>/activities', methods=['POST'])
def create_activity(session_token):
    pass


@app.route('/sessions/<session_token>/activities/<activity_token>', methods=['PUT'])
def update_activity(session_token, activity_token):
    pass


@app.route('/sessions/<session_token>/activities/<activity_token>/comments', methods=['POST'])
def create_comment(session_token, activity_token):
    pass


if __name__ == '__main__':
    app.run(port=5000)
