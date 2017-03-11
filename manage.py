#!/usr/bin/env python2.7

""" File managing all commands to manage the expert-octo-fortnight 

LICENSE: TODO

COMMANDS: TODO

USAGE: TODO

OPTIONS: TODO

"""

from functools import wraps
import logging
import logging.handlers
import os
import signal
import sys

import Flask
from flask.ext.script import Shell

from app.application import create_app, get_config

OPTIONS = docopt(__doc__) if __name__ == '__main__' else dict()

class CustomFormatter(logging.Formatter):
    LEVEL_MAP = {logging.FATAL: 'F', logging.ERROR: 'E', logging.WARN: 'W', logging.INFO: 'I', logging.DEBUG: 'D'}

    def format(self, record):
        record.levelletter = self.LEVEL_MAP[record.levelno]
        return super(CustomFormatter, self).format(record)

def setup_logging(name = None):
    """ Google-Style logging (no idea what this means)

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

    fmt = '%(levelletter)s%(asctime)s.%(msecs).03d %(process)d %(filename)s:%(lineno)d] %(message)s'
    datefmt = '%m%d %H:%M:%S'
    formatter = CustomFormatter(fmt, datefmt)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.ERROR if log_to_disk else logging.DEBUG)
    console_hanlder.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(console_handler)

    if log_to_disk:
        file_name = os.path.join(OPTIONS['--join_dir'], 'app_{}.log'.format(name))
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
    
    if OPTIONS['--config_prod']:
        config_class_string = 'app.config.Production'
    else:
        config_class_string = 'app.config.Config'
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
    setup_loggin('devserver')
    app = create_app(parse_options())
    log_messages(app, OPTIONS['--port'])
    app.run(host = '0.0.0.0', port = int(OPTIONS['--port']))

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    if not OPTIONS['--port'].isdigit():
        print('ERROR: Port should be a number.')
        sys.exit(1)
    getattr(command, 'chosen')()
    
