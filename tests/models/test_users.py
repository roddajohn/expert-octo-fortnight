""" Tests the users.py file 
"""

import pytest

from app.models.users import User

from app.models.helpers import DuplicateException

def test_insert():
    """ Tests the User insert method """

    new = User('testing@testing.com', permissions = ['testing'])

    returned = new.insert()

    assert returned.acknowledged
    assert returned.inserted_id > -1

def test_query_id_email():
    obj_id = User.query_email('testing@testing.com')._id

    assert User.query_id(obj_id).email == 'testing@testing.com'

def test_update():
    obj = User.query_email('testing@testing.com')

    obj.email = 'testing@testing.testing.com'
    obj.update()

    obj = User.query_id(obj._id)
    assert obj.email == 'testing@testing.testing.com'

    obj.email = 'testing@testing.com'
    obj.update()

def test_duplicate():
    with pytest.raises(DuplicateException):
        new = User('testing@testing.com')

        returned = new.insert()

def test_remove():
    u = User.query_email('testing@testing.com')

    result = u.remove()

    assert result.acknowledged
    assert result.deleted_count == 1
