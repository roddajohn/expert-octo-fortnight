""" Test basic things

Ensures python version is good

Checks the root route makes sure that returns HTTP 200
"""

import sys

from flask import current_app

def test_python_version():
    """ Application runs under 2.7 but not 2.6, test for 2.7.6 or greater """
    assert 2 == sys.version_info.major
    assert 7 == sys.version_info.minor
    assert 6 <= sys.version_info.micro

def test_testing_mode():
    """ Ensure TESTING = True in app.config """
    assert current_app.config['TESTING']

def test_index_200():
    """ Makes sure the front page returns HTTP 200 """

    assert '200 OK' == current_app.test_client().get('/').status
