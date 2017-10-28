""" Tests app.models.required_data.py """

import pytest

from app.models.required_data import RequiredData

def test_insert():
    """ Tests the RequiredData insert method """
    
    new = RequiredData('testing_data',
                       'TESTING_DATA',
                       'int',
                       False,
                       False,
                       ['student'])

    returned = new.insert()

    assert returned.acknowledged
    assert returned.inserted_id > -1

def test_query_id_name():
    obj_id = RequiredData.query_name('testing_data')._id

    assert RequiredData.query_id(obj_id).name == 'testing_data'

def test_update():
    obj = RequiredData.query_name('testing_data')

    obj.required = False
    obj.update()

    obj = RequiredData.query_name('testing_data')
    assert not obj.required

def test_remove():
    r = RequiredData.query_name('testing_data')

    result = r.remove()

    assert result.acknowledged
    assert result.deleted_count == 1
