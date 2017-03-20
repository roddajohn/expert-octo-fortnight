""" Flask extensions and misc extensions iniatialized here """

from flask_mail import Mail

from flask_sqlalchemy import SQLAlchemy

mail = Mail()

db = SQLAlchemy()
