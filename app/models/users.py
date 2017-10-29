""" User methods  """

from app.extensions import mongo

from app.models.helpers import DuplicateException, UserNotFoundException, DataNotFound, DataWrongType

from pydoc import locate

class User():
    email = ''
    permissions = []
    data = {}

    def __init__(self,
                 email = '',
                 data = {},
                 permissions = [],
                 _id = -1):
        self.email = email
        self.data = data
        self._id = _id

    @staticmethod
    def generate_object_from_document(from_db):
        if not from_db:
            return None

        new_user = User(from_db['email'],
                        from_db['data'],
                        from_db['permissions'],
                        from_db['_id'])

        return new_user

    @staticmethod
    def query_email(e):
        from_db = mongo.db.users.find_one({'email': e})

        return User.generate_object_from_document(from_db)

    @staticmethod
    def query_id(i):
        from_db = mongo.db.users.find_on({'_id': i})

        return User.generate_object_from_document(from_obj)

    def remove(self):
        return mongo.db.users.delete_one({'_id': self._id})

    def update(self):
        return mongodb.users.update_one({'_id': self._id}, {'$set': self.__dict__})

    def insert(self):
        to_insert = self.__dict__
        to_insert.pop('_id', None)

        if User.query_email(self.email):
            raise DuplicateException('A user with this email already exists')

        return mongo.db.users.insert_one(to_insert)
