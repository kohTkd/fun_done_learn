from flask import jsonify
import functools


def respondable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return jsonify(response.body), response.status
    return wrapper
