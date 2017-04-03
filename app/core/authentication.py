""" File managing decorators managing who is logged in and not, as well as permission handling """

from flask import g
from flask import session

import logging

from app.models.permissions import Role
from app.models.users import User

from app.blueprints import auth_mod

@auth_mod.before_request
def load_user():
    """ Loads the user from the session into the g variable 

    Runs before any request is passed to the appropriate view route using the flask before_request decorator

    If session does not contain id, sets g.user to None
    """
    
    user = None
    
    if 'id' in session:
        user = User.query.filter_by(id = session['id'])

    g.user = user
