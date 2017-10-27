""" Flask extensions and misc extensions iniatialized here 

This currently includes :mod:`flask_mail` and :mod:`flask-pymongo`
"""

from flask_mail import Mail
from flask_pymongo import PyMongo

mail = Mail()
""" The flask_mail object, to be imported and used in other parts of the project. """

mongo = PyMongo()


