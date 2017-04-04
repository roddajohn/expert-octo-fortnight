""" Tests app.core.authentication """

import pytest

from flask import g, session

from tests.models.helpers import create_test_user

def test_load_user():
    """ Tests the load_user decorator """

    user = create_test_user
    
    db.session.add(user)
    db.session.commit()

    session['id'] = user.id # This is how the load_user method loads the user

    
    
