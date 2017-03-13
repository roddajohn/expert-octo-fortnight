""" Tests the users.py file

Checks get_user(id)
Check add_user(user_data)
"""

from app.models.users import get_user, add_user, delete_user

from bson.objectid import ObjectId

user = {'username': 'testing123'}

def test_add_user():
    """ Testing the add_user function 
    
    Tests adding a user
    Tests adding the same user
    """
    id_of_user = add_user(user)
    second_id_of_user = add_user(user)

    assert type(id_of_user) is ObjectId
    assert type(second_id_of_user) is ObjectId
    assert id_of_user == second_id_of_user
    assert not None == get_user(id_of_user)

def test_get_user():
    """ Testing the get_user function """
    id_of_user = add_user(user)

    assert None == get_user(0)
    assert user['username'] == get_user(id_of_user)['username']

def test_delete_user():
    """ Testing the delete_user function """
    id_of_user = add_user(user)

    assert delete_user(id_of_user) == 1
    print id_of_user
    assert delete_user(id_of_user) == 0
