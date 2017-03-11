""" Tests the auth views defined in views/auth/controller.py """

from flask import current_app

def test_index():
    """ Tests /auth/ """
    assert '200 OK' == current_app.test_client().get('/auth/').status
