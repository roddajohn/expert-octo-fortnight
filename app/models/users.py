""" Manages all users in the Mongo db """

from app.extensions import mongo

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

    user_id = mongo.db.users.insert_one(user_data).inserted_id

    return inserted_id
    
