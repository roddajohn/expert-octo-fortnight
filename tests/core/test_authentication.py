""" Tests app.core.authentication """

import pytest

from flask import g, session

from tests.models.helpers import create_test_user
from tests.conftest import app

from app.extensions import db
from app.core.authentication import load_user, require_login, require_role

def test_require_login():
    """ Tests the require_login decorator """

    user = create_test_user()

    db.session.add(user)
    db.session.commit()
    
    def testing_function():
        return 'Success'

    with app.test_request_context(''): # Tests with proper id set
        session['id'] = user.id # This is how the load_user method loads the user
        app.preprocess_request()

        assert require_login(testing_function)() == 'Success'
        
    with app.test_request_context(''): # Tests without proper id set
        app.preprocess_request()
        assert 'Redirecting' in require_login(testing_function)().data # Redirecting to 'index' as defined in app.core.authentication

    db.session.delete(user)
    db.session.commit()
    
def test_require_role():
    """ Tests the require_role decorator """

    user = create_test_user()
    user.add_role('testing')

    db.session.add(user)
    db.session.commit()
    
    def testing_function():
        return 'Success'

    with app.test_request_context(''): # Tests with proper role
        session['id'] = user.id # This is how the load_user method loads the user
        app.preprocess_request()

        assert (require_role(testing_function, 'testing')()) == 'Success'
        
    with app.test_request_context(''): # Tests without role
        session['id'] = user.id # This is how the load_user method loads the user
        app.preprocess_request()

        user.remove_role('testing') # Removes the role to test without the desired role
        db.session.commit()
        
        assert 'Redirecting' in require_role(testing_function, 'testing')().data # Redirecting to 'index' as defined in app.core.authentication

    db.session.delete(user)
    db.session.commit()


def test_load_user():
    """ Tests the load_user pre request processor """

    user = create_test_user()
    

    db.session.add(user)
    db.session.commit()

    

    with app.test_request_context(''):
        session['id'] = user.id # This is how the load_user method loads the user
        
        load_user()
        
        assert g.user == user
        
        session['id'] = 0

        load_user()
        
        assert g.user == None

    db.session.delete(user)
    db.session.commit()
    

    
