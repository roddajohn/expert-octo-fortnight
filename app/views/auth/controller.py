from app.blueprints import auth_mod
from app.core.authentication import load_user

from flask import g

import logging

LOG = logging.getLogger(__name__)

@auth_mod.route('/')
def index():
    return 'auth blueprint test'
