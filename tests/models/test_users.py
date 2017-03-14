""" Tests the users.py file

Checks get_user(id)
Check add_user(user_data)
Check delete_user(id)
"""

from app.models.users import get_user, add_user, delete_user

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

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
    """ Testing the get_user function

    Tests retreiving a user with a clearly incorrect id
    Tests restreiving a user and confirming that the username field is correct
    """
    id_of_user = add_user(user)

    assert None == get_user(0)
    assert user['username'] == get_user(id_of_user)['username']

def test_set_password():
    """ Testing the set_password function

    Tests setting a password on a user that does exit
    Tests setting a password on a user that does not
    """

    id_of_user = add_user(user)

    set_password(id_of_user, 'password')
    user = get_user(id_of_user)

    assert user['password'] == generate_password_hash('password')

    set_password(get_user(0), 'password')

def test_delete_user():
    """ Testing the delete_user function 
    
    Tests deleting a user that exists
    Tests deleting a user that does not exist
    """
    id_of_user = add_user(user)

    assert delete_user(id_of_user) == 1
    assert delete_user(id_of_user) == 0
    
