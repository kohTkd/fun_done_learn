from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World.'}), 200

if __name__ == '__main__':
    app.run(port=5000)
