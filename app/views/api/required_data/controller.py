from app.blueprints import required_data_api_mod

from app.models.required_data import RequiredData
from app.models.users import User
from app.models.helpers import remove_id
from app.models.required_data import required_args

from flask import request, jsonify, abort

import logging

LOG = logging.getLogger(__name__)

### REQUIRED_DATA API ###

@required_data_api_mod.route('', methods = ['GET'])
def get_data():
    permission = request.args['permission'] if 'permission' in request.args else ''
    required = True if 'required' in request.args and request.args['required'] == 'True' else False

    to_return = RequiredData.get_all_required(permission) if required else RequiredData.get_all(permission)

    to_return = [remove_id(data.__dict__) for data in to_return]

    return jsonify(to_return)

@required_data_api_mod.route('/<string:name>', methods = ['GET'])
def get_data_name(name = ''):
    data = RequiredData.query_name(name)

    return jsonify(remove_id(data.__dict__))

@required_data_api_mod.route('', methods = ['PUT'])
def insert_new_data():
    for arg in required_args:
        if not arg in request.args:
            LOG.error(str(request.args))
            abort(500)

    r = RequiredData(name = request.args['name'],
                     display_name = request.args['display_name'],
                     type = request.args['type'],
                     required = bool(request.args['required']),
                     user_input = bool(request.args['user_input']),
                     permissions_applicable = request.args['permissions_applicable'].split(','),
                     visibility = request.args['visibility'].split(','))

    result = r.insert()

    return jsonify({'result': 'success'}) if result.acknowledged else jsonify({'result': 'error'})                
        
    
    

    
    
    
    
        
