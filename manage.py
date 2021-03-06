#!/usr/bin/env python2.7

""" File managing all commands to manage the expert-octo-fortnight 

LICENSE: TODO

COMMANDS: 
    devserver             Run the application using dev
    shell                 Starts a python shell in app context

USAGE:
    manage.py devserver [-p NUM] [-l DIR] [--config_prod]
    manage.py shell [--config_prod]

OPTIONS:
    --config_prod         Load the production configurations instead of development
    -p NUM --port=NUM     Flask will listen on this port number. default: 5000
    -l DIR --log_dir=DIR  Log all statements to files in this directory instead of stdout.

"""
# Python imports
from functools import wraps
from pydoc import locate
import logging
import logging.handlers
import os
import signal
import sys
import os.path
from docopt import docopt

# Flask and database imports
import flask
from flask_script import Shell
from migrate.versioning import api
from migrate.exceptions import InvalidRepositoryError, DatabaseAlreadyControlledError
import imp

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Updated
# Application imports
from app.application import create_app, get_config
from app.extensions import mongo
import app.models

#from app.models.helpers import b

OPTIONS = docopt(__doc__) if __name__ == '__main__' else dict()

class CustomFormatter(logging.Formatter):
    """ Adds the custom formatter for logging (the character at the beginning of the log) """
    LEVEL_MAP = {logging.FATAL: 'F', logging.ERROR: 'E', logging.WARN: 'W', logging.INFO: 'I', logging.DEBUG: 'D'}

    def format(self, record):
        record.levelletter = self.LEVEL_MAP[record.levelno]
        return super(CustomFormatter, self).format(record)

def setup_logging(name = None):
    """ Google-Style logging (no idea what this means -- Rodda)

    name: Appends this string to the log file filename
    """

    log_to_disk = False
    if OPTIONS['--log_dir']:
        if not os.path.isdir(OPTIONS['--log_dir']):
            print('ERROR: Directory {} does not exist.'.format(OPTIONS['--log_dir']))
            sys.exit(1)
        if not os.access(OPTIONS['--log_dir'], os.W_OK):
            print('ERROR: No permission to write to directory {}.'.format(OPTIONS['--log_dir']))
            sys.exit(1)
        log_to_disk = True

    fmt = '%(levelletter)s %(asctime)s.%(msecs).03d %(process)d %(filename)s:%(lineno)d] %(message)s'
    datefmt = '%m%d %H:%M:%S'
    formatter = CustomFormatter(fmt, datefmt)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.ERROR if log_to_disk else logging.DEBUG)
    console_handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(console_handler)

    if log_to_disk:
        file_name = os.path.join(OPTIONS['--log_dir'], 'app_{}.log'.format(name))
        file_handler = logging.handlers.TimedRotatingFileHandler(file_name, when='d', backupCount = 7)
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)

def log_messages(app, port):
    """ Log messages common to dev and production servers """

    log = logging.getLogger(__name__)
    log.info('Server is running at https://0.0.0.0:{}/'.format(port))
    log.info('Flask version: {}'.format(flask.__version__))
    log.info('DEBUG: {}'.format(app.config['DEBUG']))
    log.info('STATIC_FOLDER: {}'.format(app.static_folder))

def parse_options():
    """ Parses command line options for Flask

    Returns:
    Config instance to pass into create_app()
    """
    
    if OPTIONS and OPTIONS['--config_prod']:
        config_class_string = 'app.config.Production'
    else:
        config_class_string = 'app.config.Testing'
        
    config_obj = get_config(config_class_string)

    return config_obj

def command(func):
    """ Decorator that registers the chosen command/function.

    Instead of Flask-Script

    func: the function to decorate
    """
    @wraps(func)
    def wrapped():
        return func()

    if func.__name__ not in OPTIONS:
        raise KeyError('Cannot register {}, not mentioned in docstring/docopt.'.format(func.__name__))
    if OPTIONS[func.__name__]:
        command.chosen = func

    return wrapped

@command
def devserver():
    """ Starts the development server """
    setup_logging('devserver')
    app = create_app(parse_options())
    log_messages(app, OPTIONS['--port'])
    app.run(host = '0.0.0.0', port = int(OPTIONS['--port']))

@command
def shell():
    setup_logging('shell')
    app = create_app(parse_options())
    app.app_context().push()
    Shell(make_context=lambda: dict(app=app, db=db)).run(no_ipython=False, no_bpython=False)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0)) # Catches SIGINT and exits "theoretically" nicely
    
    if OPTIONS['--port'] and not OPTIONS['--port'].isdigit():
        print('ERROR: Port should be a number.')
        sys.exit(1)
    getattr(command, 'chosen')()
