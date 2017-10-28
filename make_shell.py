from app.application import create_app, get_config

def make_shell():
    app = create_app(get_config('app.config.Testing'))
    app.app_context().push()
