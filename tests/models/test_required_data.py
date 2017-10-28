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

def test_remove():
    r = RequiredData.query_name('testing_data')

    result = r.remove()

    assert result.acknowledged
    assert result.deleted_count == 1
