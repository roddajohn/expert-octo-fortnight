""" Configuration for pytest """

import xmlrpclib

import pytest

import os
print os.getcwd()

from app.application import create_app, get_config

from app.extensions import db

class FakeServerProxy(object):
    VALUE = None

    def __init__(self, _):
        pass

    def search(self, _):
        return self.VALUE

@pytest.fixture(autouse=True, scope='session')
def create_all():
    """ Initializes and creates the database """

    db.create_all()

@pytest.fixture(scope = 'session')
def alter_xmlrpc(request):
    """ Replaces the ServerProxy class in the xmlrpclib library with a fake class.

    Class is restored after testing.
    """

    old_method = xmlrpclib.ServerProxy
    xmlrpclib.ServerProxy = FakeServerProxy

    def func(value):
        FakeServerProxy.VALUE = VALUE
    
    def fin():
        xmlrpclib.ServerProxy = old_method
    request.addfinalizer(fin)

    return func

app = create_app(get_config('app.config.Testing'))

# Initialize the application and sets the app context so that we don't have to
app.app_context().push()
