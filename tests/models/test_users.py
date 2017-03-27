""" Tests the users.py file 

Tests creating a user
Tests all fields for a user
Tests simple querying
"""

import pytest

from app.extensions import db
from app.models.users import User

def test_users():
    """ Basic User tests

    Tests basic creation and saving of a user object, as well as basic querying """
    
    new_user = User(fname = 'testing_fname', lname = 'testing_lname')

    db.session.add(new_user)
    db.session.commit()

    query = User.query.filter_by(fname = 'testing_fname').order_by(User.id.desc()).first()

    assert query.id == new_user.id

def test_password():
    """ Basic tests on password hash

    Setting password
    Checking password 

    No need to actually save this user to the database as this simply tests class methods"""

    new_user = User(fname = 'testing_fname', lname = 'testing_lname')
    
    new_user.set_password('test')
    
    assert new_user.password is not None
    assert new_user.check_password('test')
    assert not new_user.check_password('TEST')

    

    
