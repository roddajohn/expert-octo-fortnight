""" Tests app.core.authentication """

import pytest

from flask import g, session

from tests.models.helpers import create_test_user
from tests.conftest import app

from app.extensions import db
from app.core.authentication import load_user, require_login, require_role

def test_load_user():
    """ Tests the load_user decorator """

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

    
