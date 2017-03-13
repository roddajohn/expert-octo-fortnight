""" Tests the users.py file

Checks get_user(id)
Check add_user(user_data)
"""

from app.models.users import get_user, add_user, delete_user

from bson.objectid import ObjectId

user = {'username': 'testing123'}

def test_add_user():
    id_of_user = add_user(user)
    if id_of_user == 0:
        assert delete_user(id_of_user) == 1
        id_of_user = add_user(user)

    assert type(id_of_user) is ObjectId

def test_get_user():
    id_of_user = add_user(user)
    if id_of_user == 0:
        assert delete_user(id_of_user) == 1
        id_of_user = add_user(user)

    assert None == get_user(0)
    assert user['username'] == get_user(id_of_user)['username']
