""" Manages required data for users 

Includes the RequiredData class

"""

from app.extensions import mongo

from app.models.helpers import DuplicateException

class RequiredData():
    name = ''
    display_name = ''
    type = None
    required = None
    user_input = None
    permissions_applicable = []
    visibility = []

    def __init__(self,
                 name = '',
                 display_name = '',
                 t = None,
                 required = None,
                 user_input = None,
                 permissions_applicable = [],
                 visibility = [],
                 _id = -1):
        self.name = name
        self.display_name = display_name
        self.type = t
        self.required = required
        self.user_input = user_input
        self.permissions_applicable = permissions_applicable
        self.visibility = visibility
        self._id = _id

    @staticmethod
    def generate_object_from_document(from_db):
        if not from_db:
            return None
        
        new_required_data = RequiredData(from_db['name'],
                                         from_db['display_name'],
                                         from_db['type'],
                                         from_db['required'],
                                         from_db['user_input'],
                                         from_db['permissions_applicable'],
                                         from_db['visibility'],
                                         from_db['_id'])

        return new_required_data        
    
    @staticmethod
    def query_name(n):
        from_db = mongo.db.required_data.find_one({'name': n})

        return RequiredData.generate_object_from_document(from_db)
        

    @staticmethod
    def query_id(i):
        from_db = mongo.db.required_data.find_one({'_id': i})

        return RequiredData.generate_object_from_document(from_db)

    @staticmethod
    def get_all(permission = ''):
        to_return = []

        for obj in mongo.db.required_data.find():
            if permission == '' or permission in obj['permissions_applicable']:
                to_return.append(RequiredData.generate_object_from_document(obj))

        return to_return

    @staticmethod
    def get_all_required(permission):
        all_data = RequiredData.get_all(permission)
        to_return = []

        for obj in all_data:
            if obj.required:
                to_return.append(obj)

        return to_return
                
    def remove(self):
        return mongo.db.required_data.delete_one({'_id': self._id})

    def update(self):
        return mongo.db.required_data.update_one({'_id': self._id}, {'$set': self.__dict__})

    def insert(self):
        to_insert = self.__dict__
        to_insert.pop('_id', None)

        if RequiredData.query_name(self.name):
            raise DuplicateException('A piece of required data with this name already exists')
        
        return mongo.db.required_data.insert_one(to_insert)

