""" User methods  """

from app.extensions import mongo

from app.models.helpers import DuplicateException, DataNotFound, DataWrongType, UserLacksPermission

from app.models.required_data import RequiredData

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
        self.permissions = permissions
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
        from_db = mongo.db.users.find_one({'_id': i})

        return User.generate_object_from_document(from_db)

    def remove(self):
        return mongo.db.users.delete_one({'_id': self._id})

    def update(self):
        return mongo.db.users.update_one({'_id': self._id}, {'$set': self.__dict__})

    def insert(self):
        to_insert = self.__dict__
        to_insert.pop('_id', None)

        if User.query_email(self.email):
            raise DuplicateException('A user with this email already exists')

        return mongo.db.users.insert_one(to_insert)

    def set_data(self, name, value):
        required_data = RequiredData.query_name(name)

        if not required_data:
            raise DataNotFound('Data is not found with this name')

        if not type(value) is locate(required_data.type):
            raise DataWrongType('Data is of the wrong type for this piece of data')

        valid = False
        for p in required_data.permissions_applicable:
            if p in self.permissions:
                valid = True

        if not valid:
            raise UserLacksPermission('This user does not have a permission in common with the permissions that this required data requires')

        self.data[name] = value

        return True            

        
