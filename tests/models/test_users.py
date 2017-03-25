""" Tests the users.py file 

Tests creating a user
Tests all fields for a user
Tests simple querying
"""

from app.extensions import db

from app.models.users import User

def test_users():
    new_user = User(fname = 'testing_fname', lname = 'testing_lname')

    db.session.add(new_user)
    db.session.commit()

    query = User.query.filter_by(fname = 'testing_fname').order_by(User.id.desc()).first()

    assert query.id == new_user.id

    
