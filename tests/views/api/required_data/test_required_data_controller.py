""" Tests the required_data controller file

app/views/api/required_data/controller.py """

from flask import current_app, jsonify
from app.extensions import mongo

from app.models.required_data import RequiredData

from tests.helpers import insert_testing_required_data, remove_testing_data

import json

def test_get_data():
    """ Tests / """

    response = current_app.test_client().get('/api/required_data')
    
    assert '200 OK' == response.status

    response_data = json.loads(response.data)

    required_data = mongo.db.required_data.find()
    

    for data in required_data:
        data.pop('_id')
        
        found = False
        for d in response_data:
            if data == d:
                found = True
        assert found

def test_get_data_name():
    name = insert_testing_required_data()
    
    response = current_app.test_client().get('/api/required_data/' + name)

    original_obj = RequiredData.query_name(name)

    remove_testing_data()
    
    obj = original_obj.__dict__

    obj.pop('_id')

    assert '200 OK' == response.status

    assert json.loads(response.data) == obj

def test_insert_new_data():
    data_dict = {'name': 'testing_data',
                 'display_name': 'TESTING_DATA',
                 'type': 'int',
                 'required': 'False',
                 'user_input': 'False',
                 'permissions_applicable': 'student,administrator',
                 'visibility': 'student,administrator'}
    
    response = current_app.test_client().post('/api/required_data', data = json.dumps(data_dict), content_type = 'application/json')

    assert '200 OK' == response.status

    inserted_data = RequiredData.query_name('testing_data')

    assert inserted_data is not None

    remove_testing_data()

    response = current_app.test_client().post('/api/required_data', data = json.dumps({}), content_type = 'application/json')

    assert '500 INTERNAL SERVER ERROR' == response.status

def test_update_required_data():
    new_data = insert_testing_required_data()
    
    response = current_app.test_client().put('/api/required_data/testing_data', data = json.dumps({'name': 'blah', 'type': 'str'}), content_type = 'application/json')

    assert '200 OK' == response.status

    inserted_data = RequiredData.query_name('blah')

    assert inserted_data.name == 'blah'
    assert inserted_data.type == 'str'

    inserted_data.name = 'testing_data'
    inserted_data.t = 'str'
    inserted_data.update()

    response = current_app.test_client().put('/api/required_data/this_doesnt_exist', data = json.dumps({'name': 'blah', 'type': 'str'}), content_type = 'application/json')

    assert '500 INTERNAL SERVER ERROR' == response.status

    new_response = current_app.test_client().put('/api/required_data/testing_data', data = json.dumps({'lmao': 'blahh'}), content_type = 'application/json')

    assert '500 INTERNAL SERVER ERROR' == new_response.status

def test_removing_required_data():
    response = current_app.test_client().delete('/api/required_data/testing_data')

    assert '200 OK' == response.status

    response = current_app.test_client().delete('/api/required_data/this_doesnt_exist')

    assert '500 INTERNAL SERVER ERROR' == response.status

    # For good measure
    
    remove_testing_data('blah')
    remove_testing_data()
    
    
