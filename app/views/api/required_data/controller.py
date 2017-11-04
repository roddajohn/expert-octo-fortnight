from app.blueprints import required_data_api_mod

from app.models.required_data import RequiredData
from app.models.users import User
from app.models.helpers import remove_id

from flask import request, jsonify

import logging

LOG = logging.getLogger(__name__)

### REQUIRED_DATA API ###

@required_data_api_mod.route('/data', methods = ['GET'])
def get_data():
    permission = request.args['permission'] if 'permission' in request.args else ''
    required = True if 'required' in request.args and request.args['required'] == 'True' else False

    LOG.warn(required)

    to_return = RequiredData.get_all_required(permission) if required else RequiredData.get_all(permission)

    to_return = [remove_id(data.__dict__) for data in to_return]

    return jsonify(to_return)

@required_data_api_mod.route('/data/<string:name>', methods = ['GET'])
def get_data_name(name = ''):
    data = RequiredData.query_name(name)

    return jsonify(remove_id(data.__dict__))

    
    
    
    
        
