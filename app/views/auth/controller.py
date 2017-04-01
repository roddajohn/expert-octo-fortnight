from app.blueprints import auth_mod

from flask import g

import logging

@auth_mod.route('/')
def index():
    return 'auth blueprint test'
