from app.extensions import mongo

def is_valid(key):
    from_db = mongo.db.keys.find_one({'key': key})

    return True if from_db else False
