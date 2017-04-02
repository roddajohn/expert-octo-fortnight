""" Tests the users.py file 

Tests creating a user
Tests all fields for a user
Tests simple querying
Tests password setting and checking
Tests role setting and checking
"""

from app.extensions import db
from app.models.users import User
from tests.models.helpers import create_test_user, create_test_role

def test_users():
    """ Basic User tests

    Tests basic creation and saving of a user object, as well as basic querying 
    """
    
    new_user = create_test_user()

    db.session.add(new_user)
    db.session.commit()

    query = db.session.query(User).filter_by(fname = 'testing').order_by(User.id.desc()).first()

    assert query.id == new_user.id

def test_password():
    """ Basic tests on password hash

    Setting password
    Checking password 

    No need to actually save this user to the database as this simply tests class methods
    """

    new_user = create_test_user()
    
    new_user.set_password('test')
    
    assert new_user.password is not None
    assert new_user.check_password('test')
    assert not new_user.check_password('TEST')

def test_role_checking():
    """ Basic role check test
    
    Checks the check_role function
    """

    u = create_test_user()
    r = create_test_role()

    u.roles.append(r)

    assert u.check_role(r.role)
    assert not u.check_role('')

def test_role_adding():
    """ Tests the add_role method """

    u = create_test_user()
    u.add_role('test')

    assert u.check_role('test')
    assert not u.check_role('')

def test_role_removing():
    """ Tests the remove_role method """

    u = create_test_user()
    db.session.add(u)
    db.session.commit()
    
    u.add_role('test')

    assert u.remove_role('test')
    assert not u.remove_role('test')
    assert not u.remove_role('')

    db.session.delete(u)
    db.session.commit()

def test_repr():
    """ Tests the __repr__ """

    u = create_test_user()
    db.session.add(u)
    db.session.commit()

    #assert str(u) == '<

