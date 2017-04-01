""" File managing decorators managing who is logged in and not, as well as permission handling """

from app.models.permissions import Role
from app.models.users import User

from app.application import app

@app.before_request
def load_user():
    """ Loads the user from the session into the g variable 

    If session does not contain id, sets g.user to None
    """
    
    user = None
    
    if session['id']:
        user = User.query.filter_by(id = session['id'])

    g.user = user
        
        
