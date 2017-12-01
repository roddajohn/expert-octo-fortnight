""" Tests the app/models/helpers.py file """

from app.models.users import User

from app.models.helpers import remove_id

def test_remove_id():
    """ Tests removing the id from a database object """

    new = User('testing@testing.com', permissions = ['testing'])

    returned = new.insert()

    obj = User.query_email('testing@testing.com')

    obj.remove()

    obj = remove_id(obj.__dict__)

    assert not '_id' in obj

    
        

