""" File managing decorators managing who is logged in and not, as well as permission handling """

from flask import g
from flask import session

import logging

from app.models.permissions import Role
from app.models.users import User

from app.blueprints import auth_mod

import functools

@auth_mod.before_app_request
def load_user():
    """ Loads the user from the session into the g variable 

    Runs before any request is passed to the appropriate view route using the flask before_request decorator

    If session does not contain id, sets g.user to None
    """
    
    user = None
    
    if 'id' in session:
        user = User.query.filter_by(id = session['id'])

    g.user = user

def require_login(f):
    """ Authentication decorator

    :returns: A rendered page to display, either through the view route that it is decorating, or a page with a flashed message.

    If user is logged in run the route

    If user is not logged in display a message to the user and redirect to the 'index' route
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not g:
            flash('You are not logged in')
            return redirect('index')
        return f(*args, **kwargs)
    return wrapper

@require_login
def require_role(f, role):
    """ Authentication decorator
    
    :param role: The role to check
    :type role: str
    :returns: A rendered page to display, either through the view route that it is decorating, or a page with a flashed message.

    If the user has the requisite role, call the view route which this function decorates.

    If user does not have the requisite role, display a message to the user and redirect to the 'index' route
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not g.check_role(role):
            flash('You do not have the required role')
            return redirect('index')
        return f(*args, **kwargs)
    return wrapper




