""" Tests the users.py file 
"""

import pytest

from app.models.users import User
from app.models.required_data import RequiredData

from app.models.helpers import DuplicateException, DataNotFound, DataWrongType, UserLacksPermission

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

def test_set_data():
    r = RequiredData('testing',
                     'Testing',
                     'int',
                     False,
                     False,
                     ['testing'])

    r.insert()

    u = User('testing@testing.com',
             permissions = ['testing'])

    u.insert()

    u = User.query_email('testing@testing.com')

    with pytest.raises(DataNotFound):
        u.set_data('blah_blah_blah', 8)

    with pytest.raises(DataWrongType):
        u.set_data('testing', False)

    with pytest.raises(UserLacksPermission):
        u.permissions = []
        u.update()

        u.set_data('testing', 8)

    u.permissions = ['testing']
    u.update()

    u.set_data('testing', 8)
    u.update()

    u = User.query_email('testing@testing.com')

    assert u.data['testing'] == 8

    u.remove()
    r.remove()
    
                     
