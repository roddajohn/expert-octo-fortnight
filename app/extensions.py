""" Flask extensions and misc extensions iniatialized here """

from flask_mail import Mail
from flask_pymongo import PyMongo

mail = Mail()
mongo = PyMongo()
