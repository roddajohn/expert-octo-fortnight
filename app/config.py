class HardCoded(object):
    """ Constants to be used throughout the application

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their extensions goes here.
    """

class CeleryConfig(HardCoded):
    """ Celery Configuration """
    
    # TODO

class MongoConfig(CeleryConfig):
    """ Mongo Configuration """
    
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'arista'
    
class Config(MongoConfig):
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
