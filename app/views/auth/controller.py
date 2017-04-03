from app.blueprints import auth_mod

from flask import g

import logging

LOG = logging.getLogger(__name__)

@auth_mod.route('/')
def index():
    LOG.info(g.user)
    
    return 'auth blueprint test'
