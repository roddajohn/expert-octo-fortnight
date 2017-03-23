""" User model """

from sqlalchemy import Column, String, Text

from app.models.helpers import Base

class User(Base):
    """ User model """

    fname = Column(String(64), unique = False, nullable = False)
    lname = Column(String(64), unique = False, nullable = False)
