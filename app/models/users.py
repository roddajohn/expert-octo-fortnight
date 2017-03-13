""" Manages all users in the Mongo db """

from app.extensions import mongo
from pymongo.errors import DuplicateKeyError

def get_user(id):
    """ Returns a user dictionary

    id: The id of the user to find

    Returns:
    The dictionary retrieved from the database corresponding to the user with id <id>
    """

    user = mongo.db.users.find_one({'_id' : id})

    return user

def add_user(user_data):
    """ Adds a user to the database
    
    user_data: dictionary of user data
    Keys:
        TODO

    Returns: 
    id of user if success, 0 if failure
    """

    try:
        user_id = mongo.db.users.insert_one(user_data).inserted_id
    except DuplicateKeyError:
        return 0

    return user_id

def delete_user(id):
    """ Deletes a user from the database
    
    id: The id of the user to delete

    Returns:
    True if the delete was successful
    Flase if the delete was not successful
    """

    user = get_user(id)
    result = mongo.db.users.delete_one(user).deleted_count

    return result
