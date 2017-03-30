""" Permissions models

Currently just Role """

from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.helpers import Base

class Role(Base):
    """ Role base to store a user's role """

    role = Column(String(64), unique = False, nullable = False)
    """ Column to store the role, as a string.

    Current values used:
     - 'user'
     - 'admin'
    """

    user_id = Column(Integer, ForeignKey('user.id'))
    """ Column storing the ForeignKey for the user """
    
    user = relationship('User', back_populates = 'roles')
    """ Relationship Column creating the many-to-one relationship """

    
