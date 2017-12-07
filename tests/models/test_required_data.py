""" Tests app.models.required_data.py """

import pytest

from app.models.required_data import RequiredData
from app.models.helpers import DuplicateException

from tests.helpers import insert_testing_required_data, remove_testing_data

def test_insert():
    """ Tests the RequiredData insert method """

    insert_testing_required_data()
    
def test_query_id_name():
    obj_id = RequiredData.query_name('testing_data')._id

    assert RequiredData.query_id(obj_id).name == 'testing_data'

def test_update():
    obj = RequiredData.query_name('testing_data')

    obj.required = False
    obj.update()

    obj = RequiredData.query_name('testing_data')
    assert not obj.required

def test_duplicate():
    with pytest.raises(DuplicateException):
        new = RequiredData('testing_data',
                           'TESTING_DATA',
                           'int',
                           False,
                           False,
                           ['student'])
        
        returned = new.insert()
        
def test_remove():
    remove_testing_data()


def test_get_all():
        new = RequiredData('testing_data_one',
                           'TESTING_DATA',
                           'int',
                           False,
                           False,
                           ['testing_student'])
        
        returned = new.insert()

        new = RequiredData('testing_data_two',
                           'TESTING_DATA',
                           'int',
                           True,
                           False,
                           ['testing_student'])
        
        returned = new.insert()

        get_all = RequiredData.get_all('testing_student')

        assert len(get_all) == 2

        get_all_required = RequiredData.get_all_required('testing_student')

        assert len(get_all_required) == 1

        # Cleanup
        RequiredData.query_name('testing_data_one').remove()
        RequiredData.query_name('testing_data_two').remove()
        
    
