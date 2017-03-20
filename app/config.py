""" All configuration values for the app """

from urllib import quote_plus

class HardCoded(object):
    """ Constants to be used throughout the application

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their extensions goes here.
    """

    _SQLALCHEMY_DATABASE_DATABASE = 'arista'
    _SQLALCHEMY_DATABASE_HOSTNAME = 'localhost'
    _SQLALCHEMY_DATABASE_PASSWORD = 'password'
    _SQLALCHEMY_DATABASE_USERNAME = 'arista_website'

class CeleryConfig(HardCoded):
    """ Celery Configuration """
    
    # TODO

class SQLConfig(CeleryConfig):
    """ SQL Alchemy Configuration """
    
    SQLALCHEMY_DATABASE_URI = property(lambda self: 'mysql://{u}:{p}@{h}/{d}'.format(
        d=quote_plus(self._SQLALCHEMY_DATABASE_DATABASE), h=quote_plus(self._SQLALCHEMY_DATABASE_HOSTNAME),
        p=quote_plus(self._SQLALCHEMY_DATABASE_PASSWORD), u=quote_plus(self._SQLALCHEMY_DATABASE_USERNAME)
    ))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
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

class Production(Config):
    DEBUG = False
    MAIL_SUPPRESS_SEND = False
