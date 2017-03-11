from app.blueprints import public_mod

@public_mod.route('/')
def index():
    return 'public blueprint test'
