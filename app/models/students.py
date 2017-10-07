""" Definition of the Student model. """

from sqlalchemy import Column, Integer

from app.models.users import User

class Student(Base):
    """ Student model for use with sqlalchemy. """

    __name__ = 'Student'
    """ Name of the class (for the benefit of the __repr__ method) """

    osis = Column(Integer, unique = True, nullable = False)
    """ Column to store osis number """
