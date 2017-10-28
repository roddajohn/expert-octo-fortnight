""" Manages required data for users 

Includes the RequiredData class

"""

from app.extensions import mongo

from app.models.helpers import DuplicateException

class RequiredData():
    name = ''
    display_name = ''
    t = None
    required = None
    user_input = None
    permissions_applicable = []

    def __init__(self,
                 name = '',
                 display_name = '',
                 t = None,
                 required = None,
                 user_input = None,
                 permissions_applicable = [],
                 _id = -1):
        self.name = name
        self.display_name = display_name
        self.t = t
        self.required = required
        self.user_input = user_input
        self.permissions_applicable = permissions_applicable
        self._id = _id

    def generate_object_from_document(from_db):
        if not from_db:
            return None
        
        new_required_data = RequiredData(from_db['name'],
                                         from_db['display_name'],
                                         from_db['type'],
                                         from_db['required'],
                                         from_db['user_input'],
                                         from_db['permissions_applicable'],
                                         from_db['_id'])

        return new_required_data        
    
    @staticmethod
    def query_name(n):
        from_db = mongo.db.required_data.find_one({'name': n})

        return generate_object_from_document(from_db)
        

    @staticmethod
    def query_id(i):
        from_db = mongo.db.required_data.find_one({'_id': i})

        return generate_object_from_document(from_db)

    def update(self):
        return mongo.db.required_data.update_one({'_id': self._id}, self.__dict__)

    def insert(self):
        to_insert = self.__dict__
        to_insert.pop('_id', None)

        if query_name(to_insert.name):
            raise DuplicateException('A piece of required data with this name already exists')
        
        return mongo.db.required_data.insert_one(to_insert)

def add_required_data(name,
                      display_name,
                      t = 'str',
                      required = False,
                      user_input = False,
                      permissions_applicable = ['student']):
    """ This method creates and saves a new piece of required data """
    
    new_required_data = {}

    test_exists = mongo.db.required_data.find_one({'name': name, 'display_name': display_name})

    if test_exists:
        raise DuplicateException('A required_data with this name and display_name already exists')
    
    new_required_data['name'] = name
    new_required_data['display_name'] = display_name
    new_required_data['type'] = t
    new_required_data['required'] = False
    new_required_data['user_input'] = False
    new_required_data['permissions_applicable'] = permissions_applicable

    return mongo.db.required_data.insert_one(new_required_data)

def all_data(permission):
    """ Returns a list of all the data, for a permission """

    required_data = mongo.db.required_data.find()

    to_return = []

    for data in required_data:
        if permission in data['permissions_applicable']:
            to_return.append(data)

    return to_return

def required_data(permission):
    """ Returns a list of all the required data, for a permission """

    required_data = mongo.db.required_data.find()

    to_return = []

    for data in required_data:
        if permission in data['permissions_applicable'] and data['required']:
            to_return.append(data)

    return to_return

def is_required(name, permission):
    """ Returns if a piece of data is required or not for a permission """

    required = False
    
    for e in required_data(permission):
        required = required or name == e['name']
        
    return required

def get_data(name):
    """ Returns the data dictionary for a specific name """

    data = mongo.db.required_data.find({'name': name})

    return data

def user_input_allowed(permission):
    """ Returns a simple list of the names of the required data which a user can enter """

    required_data = mongo.db.reqired_data.find()

    to_return = []

    for data in required_data:
        if permission in data['permissions_applicable'] and data['user_input']:
            to_return.append(data['name'])

    return to_return

    
