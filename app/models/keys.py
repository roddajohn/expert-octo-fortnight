""" Key class / methods """

from app.extensions import mongo

from app.models.helpers import DuplicateException

class Key():
    key = ''
    _id = -1

    def __init__(self,
                 key = '',
                 _id = -1):
        self.key = key
        self._id = _id

    def insert(self):
        to_insert = self.__dict__
        to_insert.pop('_id', None)

        if mongo.db.keys.find_one({'key': self.key}):
            raise DuplicateException('This key is already saved in the database')

        return mongo.db.keys.insert_one(to_insert)

