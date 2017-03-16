""" Tests the users.py file

Checks get_user(id)
Check add_user(user_data)
Check delete_user(id)
"""

from app.models.users import get_user, add_user, delete_user, set_password, check_password

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

import pytest

@pytest.fixture
def user():
    """ A pytest fixture for a sample user dictionary """
    
    return {'username': 'testing123'}

def test_add_user(user):
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

def test_get_user(user):
    """ Testing the get_user function

    Tests retreiving a user with a clearly incorrect id
    Tests restreiving a user and confirming that the username field is correct
    """
    id_of_user = add_user(user)

    assert None == get_user(0)
    assert user['username'] == get_user(id_of_user)['username']

def test_set_password(user):
    """ Testing the set_password function

    Tests setting a password on a user that does exit
    Tests setting a password on a user that does not
    """

    id_of_user = add_user(user)

    set_password(id_of_user, 'password')
    user = get_user(id_of_user)

    assert user['password'] is not None

def test_delete_user(user):
    """ Testing the delete_user function 
    
    Tests deleting a user that exists
    Tests deleting a user that does not exist
    """
    id_of_user = add_user(user)

    assert delete_user(id_of_user) == 1
    assert delete_user(id_of_user) == 0

def test_set_password(user):
    """ Testing the check_password function
    
    Tests checking a password that is correct
    Tests checking a password that is not correct
    Tests checking a password on an invalid id
    """

    id_of_user = add_user(user)
    set_password(id_of_user, 'password')
    
    assert check_password(id_of_user, 'password') == True
    assert check_password(id_of_user, 'this_should_fail') == False

    # Create a random 24 character object id to check checking password on a user which doesn't exist
    assert check_password(ObjectId('101010101010101010101010'), 'this_should_fail') == False
    
