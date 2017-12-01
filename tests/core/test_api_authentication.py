""" This tests app/core/api_authentication.py """

from app.models.keys import Key
from app.core.api_authentication import is_valid

from app.extensions import mongo

def test_is_valid():
    testing_key = Key('testing_key')

    testing_key.insert()

    assert is_valid('testing_key')
    assert not is_valid('invalid_testing_key')

def test_cleanup():
    mongo.db.keys.remove({'key': 'testing_key'})
