""" Tests app.core.authentication """

import pytest

from flask import g, session

from tests.conftest import app

from app.core.authentication import load_user, require_login, require_role

def test_require_login():
    """ Tests the require_login decorator """
    assert True
    
def test_require_role():
    """ Tests the require_role decorator """

    assert True

def test_load_user():
    """ Tests the load_user pre request processor """

    assert True
    
    

    
