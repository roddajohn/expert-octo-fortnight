""" Definition of the User model.  """

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.helpers import Base
from app.models.permissions import Role
from app.extensions import db

class User(Base):
    """ User model for use with sqlalchemy. """

    def __repr__(self):
        """ __repr__ definition for the User model

        Should display as (for user with id 1): <User ID: 1>
        """
        return "<User ID: %d>" % self.id

    __tablename__ = 'user'
    """
    Sets the tablename to not be users_role and instead just be user
    """

    fname = Column(String(64), unique = False, nullable = False)
    """ Column to store first name. """
    
    lname = Column(String(64), unique = False, nullable = False)
    """ Column to store last name. """

    password = Column(String(128), unique = False, nullable = True)
    """ Column to store hashed password. """

    roles = relationship('Role', backref = 'user')
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
        :type pwd: str
        :returns: bool -- true if the password is valid, false if otherwise.
        """
        
        return check_password_hash(self.password, pwd)

    def add_role(self, role):
        """ Adds the role to the user

        :param role: The role to add.
        :type role: str
        """

        self.roles.append(Role(role = role))
        db.session.commit()

    def remove_role(self, role):
        """ Removes the role from the user

        Returns true if the user had the role and successfully deleted it.
        Returns false if the user doesn't have the role.

        :param role: The role to remove.
        :type role: str
        :returns: bool - true if the role was successfully deleted, false if the user didn't have the role
        """
        deleted = False

        for r in self.roles:
            if r.role == role:
                db.session.delete(r)
                deleted = True
                
        db.session.commit()

        return deleted

    def check_role(self, role):
        """ Checks the role for a user.

        :param role: The role to check.
        :type role: str
        :returns: bool -- true if the user has the role, false if otherwise
        """
        
        for r in self.roles:
            if r.role == role:
                return True
        return False
            
