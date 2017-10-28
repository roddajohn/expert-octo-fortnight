""" Tests app.models.required_data.py """

from app.models.required_data import RequiredData

def test_insert():
    new = RequiredData('testing_data',
                       'TESTING_DATA',
                       'int',
                       False,
                       False,
                       ['student'])

    returned = new.insert()

    assert returned.acknowledged
    assert returned.inserted_id > -1
