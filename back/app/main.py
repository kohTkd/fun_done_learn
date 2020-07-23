from flask import Flask
from flask_cors import CORS
from app.controllers.routers import sessions_router
from app.controllers.routers.sessions import activities_router
from app.controllers.routers.sessions import notes_router
from app.controllers.routers.sessions.activities import placement_router

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(sessions_router.app)
app.register_blueprint(activities_router.app)
app.register_blueprint(notes_router.app)
app.register_blueprint(placement_router.app)

if __name__ == '__main__':
    app.run(port=5000)
