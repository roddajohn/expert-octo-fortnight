""" Permissions models

Currently just Role """

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.helpers import Base
from app.extensions import db

class Role(Base):
    """ Role base to store a user's role """

    def __repr__(self):
        """ __repr__ definition for the Role model
        
        Should display as (for role with id 1): <Role ID: 1>
        """
        return "<Role ID: %d" % self.id 

    __tablename__ = 'role'
    """
    Sets the tablename to not be permissions_role and instead be just role
    """

    role = Column(String(64), unique = False, nullable = False)
    """ Column to store the role, as a string.

    Current values used:
     - 'user'
     - 'admin'
    """

    user_id = Column(Integer, ForeignKey('user.id'))
    """ Column storing the ForeignKey for the user """

    def __repr__(self):
        """ __repr__ definition for the Role model

        Should display as (for the role with id 1): <Role ID: 1>
        """
        return '<Role ID: %d>' % self.id
