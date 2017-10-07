""" Permissions models

Currently just Role """

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.helpers import Base
from app.extensions import db

class Role(Base):
    """ Role base to store a user's role """

    __name__ = 'Role'
    """ Name of the class (for the benefit of the __repr__ method) """
    
    role = Column(String(64), unique = False, nullable = False)
    """ Column to store the role, as a string.

    Current values used:
     - 'user'
     - 'admin'
    """

    user_id = Column(Integer, ForeignKey('user.id'))
    """ Column storing the ForeignKey for the user """
