""" Manages all users in the Mongo db """

from app.extensions import mongo

from pymongo.errors import DuplicateKeyError

from werkzeug.security import generate_password_hash, check_password_hash

def set_password(id, password):
    """ Sets the password of a user

    The password is hashed using werkzeug

    id: The id of the user to set the password of
    password: The plaintext string password
    """
    
    return mongo.db.users.update(
        { '_id' : id },
        { '$set': { 'password' : generate_password_hash(password) } }
    )
    
def get_user(id):
    """ Returns a user dictionary

    id: The id of the user to find

    Returns:
    The dictionary retrieved from the database corresponding to the user with id <id>
    """

    user = mongo.db.users.find_one({'_id' : id})

    return user

def check_password(id, password):
    """ Checks the password of a user

    Uses the werkzeug check_password_hash method

    id: The id of the user to check the password against
    password: The plaintext string password to test
    """

    user = get_user(id)
    if not user:
        return False
    return check_password_hash(user['password'], password)

def add_user(user_data):
    """ Adds a user to the database
    
    user_data: dictionary of user data
    See documentation for more information
    
    Returns: 
    id of user is success, if a duplicate key error is thrown, id of identical object is thrown
    """

    try:
        user_id = mongo.db.users.insert_one(user_data).inserted_id
    except DuplicateKeyError:
        user_id = mongo.db.users.find_one(user_data)['_id']

    return user_id

def delete_user(id):
    """ Deletes a user from the database
    
    id: The id of the user to delete

    Returns:
    Number of matched items deleted
    """

    user = get_user(id)
    if not user:
        return 0

    result = mongo.db.users.delete_many(user).deleted_count

    return result
