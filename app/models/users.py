""" User methods  """

from app.extensions import mongo

from app.models.helpers import DuplicateException, UserNotFoundException, DataNotFound, DataWrongType
from app.models.required_data import get_data

from pydoc import locate

def add_user(email, permissions = []):
    """ This method creates and saves a new user """

    new_user = {}

    test_exists = mongo.db.users.find_one({'email': email})

    if test_exists:
        raise DuplicateException('A user with this email already exists')

    new_user['email'] = email
    new_user['permissions'] = permissions
    new_user['data'] = {}

    return mongo.db.users.insert_one(new_user)

def get_user_id(i):
    """ This method returns a user object by id """

    return mongo.db.users.find_one({'_id': i})

def get_user_email(e):
    """ This method returns a user object by email """

    return mongo.db.users.find_one({'email': e})

def update_data_id(name, data, i):
    """ This, given a data name and data to update, and a user id, will update the data with the new data for the specific user id """
    
    user = get_user_id(i)

    if not user:
        raise UserNotFoundException('User lookup by id failed')

    for permission in user['permissions_applicable']:
        found = False

        if is_required(name, permission):
            found = True

    if not found:
        raise DataNotFound('This data is not in the data database')

    if not type(data) == locate(get_data(name)['type']):
        raise DataWrongType('This data is of the wrong type')

    user['data'][name] = data
        
    return mongo.db.users.update_one({'_id': i}, user)
    

    

