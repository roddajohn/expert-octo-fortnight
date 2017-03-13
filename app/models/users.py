""" Manages all users in the Mongo db """

from app.extensions import mongo

def get_user(id):
    """ Returns a user dictionary

    id: The id of the user to find

    Returns:
    The dictionary retrieved from the database corresponding to the user with id <id>
    """

    user = mongo.db.users.find_one({'id' : id})

    return user
