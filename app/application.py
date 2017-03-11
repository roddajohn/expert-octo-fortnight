from importlib import import_module
import locale
import os

import app as app_root
from app.blueprints import all_blueprints
from app.extensions import mail

from flask import Flask

APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')

def get_config(config_class_string):
    """ Load the Flask config from a class """
    config_module, config_class = config_class_string.rsplit('.', 1)

    config_class_object = getattr(import_module(config_module), config_class)
    config_obj = config_class_object()

    return config_obj

def create_app(config_obj):
    """ Flask application factory.  Inializes and returns the Flask application.

    This is where blueprints are registered.

    Returns:
    The initialized Flask application.
    """

    # Basic Flask initialization, loads the config from the config obj
    app = Flask(__name__, template_folder = TEMPLATE_FOLDER, static_folder = STATIC_FOLDER)
    config_dict = dict([(k, getattr(config_obj, k)) for k in dir(config_obj) if not k.startswith('_')])
    app.config.update(config_dict)

    # Setups blueprints
    for blueprint in all_blueprints:
        import_module(blueprint.import_name)
        app.register_blueprint(blueprint)

    # Initializes helpers (like mail, celery, etc)
    mail.init_app(app)

    # Activates the middleware
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    with app.app_context():
        import_module('app.middleware')


    # Returns the app instance
    return app
