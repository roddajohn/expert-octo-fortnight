""" Provides helpers for testing the models

create_user() -- returns the created user object
create_role(role) -- returns the created role object
"""

from app.extensions import db
from app.models.users import User
from app.models.permissions import Role

def create_test_role():
    """ Creates and returns a testing role

    :returns: app.models.permissions.Role the created Role object
    """

    r = Role(role = 'test')

    return r

def create_test_user():
    """ Creates and returns a testing user 
    
    :returns: app.models.user.User the created user object
    """

    u = User(fname = 'testing', lname = 'blah')

    return u
