""" Helpers for api calls """

from flask import jsonify

from functools import wraps

def api(f):
    @wraps(f)
    def make_response_proper(*args, **kwargs):
        return jsonify(f(*args, **kwargs))
    return make_response_proper

def status_success(success):
    return jsonify({'result': 'success'}) if success else jsonify({'result': 'error'})
