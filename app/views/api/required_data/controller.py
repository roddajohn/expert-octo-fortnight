from app.blueprints import required_data_api_mod

from app.models.required_data import RequiredData
from app.models.users import User
from app.models.helpers import remove_id
from app.models.required_data import required_args

from app.views.api.helpers import api, status_success

from flask import request, jsonify, abort

import logging

LOG = logging.getLogger(__name__)

### REQUIRED_DATA API ###

@required_data_api_mod.route('', methods = ['GET'])
@api
def get_data():
    permission = request.args['permission'] if 'permission' in request.args else ''
    required = True if 'required' in request.args and request.args['required'] == 'True' else False

    to_return = RequiredData.get_all_required(permission) if required else RequiredData.get_all(permission)

    to_return = [remove_id(data.__dict__) for data in to_return]

    return to_return

@required_data_api_mod.route('/<string:name>', methods = ['GET'])
@api
def get_data_name(name = ''):
    data = RequiredData.query_name(name)

    return remove_id(data.__dict__) if data else {} 

@required_data_api_mod.route('', methods = ['POST'])
def insert_new_data():
    for arg in required_args:
        if not arg in request.json:
            LOG.error(str(arg))
            abort(500)

    r = RequiredData(name = request.json['name'],
                     display_name = request.json['display_name'],
                     t = request.json['type'],
                     required = bool(request.json['required']),
                     user_input = bool(request.json['user_input']),
                     permissions_applicable = request.json['permissions_applicable'].split(','),
                     visibility = request.json['visibility'].split(','))

    result = r.insert()

    return status_success(result.acknowledged)
        
@required_data_api_mod.route('/<string:name>', methods = ['PUT'])
def update_required_data(name = ''):
    r = RequiredData.query_name(name)

    if not r:
        abort(500)

    for arg in request.json:
        try:
            setattr(r, arg, type(getattr(r, arg))(request.json[arg]))
        except:
            LOG.error('Executed the try except statement')
            abort(500)

    r.update()

    return status_success(True)

    
    
    
    
    
        
