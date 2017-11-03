from app.blueprints import api_mod

from app.models.required_data import RequiredData
from app.models.users import User

from flask import request

import logging

LOG = logging.getLogger(__name__)

### REQUIRED_DATA API ###

@api_mod.route('/data', methods = ['GET'])
def get_data():
    permission = request['permission'] if 'permission' in request else ''

    return jsonify(RequiredData.get_all(permission))

    
    
    
    
        
