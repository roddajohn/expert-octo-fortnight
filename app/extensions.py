""" Flask extensions and misc extensions iniatialized here 

This currently includes :mod:`flask_mail` and :mod:`flask_sqlalchemy`
"""

from flask_mail import Mail

from flask_sqlalchemy import SQLAlchemy

mail = Mail()
""" The flask_mail object, to be imported and used in other parts of the project. """

db = SQLAlchemy()
""" The flask_sqlalchemy object, to be imported and used in other parts of the project. """

