from app.blueprints import required_data_api_mod

from app.views.api.helpers import api, status_success

from flask import request, jsonify, abort

import logging

LOG = logging.getLogger(__name__)

### REQUIRED_DATA API ###

@required_data_api_mod.route('', methods = ['GET'])
@api
def get_data():
    return 'False'

@required_data_api_mod.route('/<string:name>', methods = ['GET'])
@api
def get_data_name(name = ''):
    return 'False'

@required_data_api_mod.route('', methods = ['POST'])
def insert_new_data():
    return 'False'
        
@required_data_api_mod.route('/<string:name>', methods = ['PUT'])
def update_required_data(name = ''):
    return 'False'

@required_data_api_mod.route('/<string:name>', methods = ['DELETE'])
def delete_required_data(name = ''):
    return 'False'
    

    
    
    
    
    
        
