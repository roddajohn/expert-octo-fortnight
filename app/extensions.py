""" Flask extensions and misc extensions iniatialized here 
ppppp
This currently includes :mod:`flask_mail` and :mod:`flask-pymongo`
"""

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
""" The flask_mail object, to be imported and used in other parts of the project. """

db = SQLAlchemy()
""" The db object, to be imported and used in other parts of the project. """




