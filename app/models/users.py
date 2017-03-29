""" User model """

from sqlalchemy import Column, String, Text
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.helpers import Base
from app.extensions import db

class User(Base):
    """ User model """

    fname = Column(String(64), unique = False, nullable = False)
    lname = Column(String(64), unique = False, nullable = False)

    password = Column(String(128), unique = False, nullable = True)

    def set_password(self, pwd):
        """ Sets the password for a user

        Uses the werkzeug hash method

        pwd: The password to hash """
        
        self.password = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        """ Checks a password

        Uses the werkzeug check password method

        pwd: The password to test """
        
        return check_password_hash(self.password, pwd)
        
