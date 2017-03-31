""" Definition of the User model.  """

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.helpers import Base
from app.extensions import db

class User(Base):
    """ User model for use with sqlalchemy. """

    fname = Column(String(64), unique = False, nullable = False)
    """ Column to store first name. """
    
    lname = Column(String(64), unique = False, nullable = False)
    """ Column to store last name. """

    password = Column(String(128), unique = False, nullable = True)
    """ Column to store hashed password. """

    #roles = relationship('Role')
    """ Relationship Column creating the one-to-many relationship """

    def set_password(self, pwd):
        """ Sets the password for a user.

        Uses the werkzeug hash method to hash the password.

        :param pwd: The new password
        :type pwd: str
        """
        
        self.password = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        """ Checks a password.

        Uses the werkzeug check password method.

        :param pwd: The password to check.
        :type pwd: str.
        :returns: bool -- true if the password is valid, false if otherwise.
        """
        
        return check_password_hash(self.password, pwd)
