from flask import jsonify


def respondable(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return jsonify(response.body), response.status
    return wrapper
