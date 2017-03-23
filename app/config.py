""" All configuration values for the app """

import os

class HardCoded(object):
    """ Constants to be used throughout the application

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their extensions goes here.
    """

    basedir = os.path.abspath(os.path.dirname(__file__))
    
class CeleryConfig(HardCoded):
    """ Celery Configuration """
    
    # TODO

class SQLConfig(CeleryConfig):
    """ SQL Alchemy Configuration """
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(HardCoded.basedir, 'data/app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(HardCoded.basedir, 'migrations')
    
class Config(SQLConfig):
    """ Flask Configuration global to all environments """

    DEBUG = True
    TESTING = False
    SECRET_KEY = 'This is a very very secret key'

    # TODO
    MAIL_SERVER = 'smtp.localhost.test'
    MAIL_DEFAULT_SENDER = 'admin@demo.test'
    MAIL_SUPPRESS_SEND = True

class Testing(Config):
    TESTING = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production(Config):
    DEBUG = False
    MAIL_SUPPRESS_SEND = False

    SQLALCHMEY_TRACK_MODIFICATIONS = False
