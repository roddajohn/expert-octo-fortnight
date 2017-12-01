""" Tests the app/models/keys.py file """

import pytest

from app.models.keys import Key
from app.models.helpers import DuplicateException

from app.extensions import mongo

def test_insert():
    """ Tests the Key's insert method """

    new = Key('testing_key')

    returned = new.insert()

    assert returned.acknowledged
    assert returned.inserted_id > -1

def test_duplicate():
    with pytest.raises(DuplicateException):
        new = Key('testing_key')

        returned = new.insert()

    mongo.db.keys.remove({'key': 'testing_key'})
