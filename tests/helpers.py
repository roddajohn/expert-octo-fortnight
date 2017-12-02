""" Some helpers for working with some things :) """

from app.models.required_data import RequiredData

original_name = 'testing_data'

def insert_testing_required_data(name = original_name):
    new = RequiredData(name,
                       'TESTING_DATA',
                       'int',
                       False,
                       False,
                       ['student'])
    
    returned = new.insert()
    
    assert returned.acknowledged
    assert returned.inserted_id > -1

    return name

def remove_testing_data(name = original_name):
    original_obj = RequiredData.query_name(name)
    
    result = original_obj.remove()

    assert result.acknowledged
    assert result.deleted_count == 1



