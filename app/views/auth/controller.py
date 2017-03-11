from app.blueprints import auth_mod

@auth_mod.route('/')
def index():
    return 'auth blueprint test'
