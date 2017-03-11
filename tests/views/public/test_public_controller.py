""" Tests the public views defined in views/public/controller.py """

from flask import current_app

def test_index():
    """ Tests / """
    assert '200 OK' == current_app.test_client().get('/').status
