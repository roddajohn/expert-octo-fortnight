""" File managing students

Current methods:
create_student(fname, lname, password, email, osis)
"""

from app.models.users import User
from app.extensions import db

def create_student(fname, lname, password = '', email = '', osis = -1):
    """ create_student(fname, lname, password = '', email = '', osis = -1)
    Method to create a student object and return that object.

    :param fname: First name of the student to create (required)
    :type fname: str
    :param lname: Last name of the student to create (required)
    :type lname: str
    :param password: Password for the student to create
    :type password: str
    :param email: Email for the student to create
    :type email: str
    :param osis: OSIS for the student to create
    :type osis: int
    :returns: The new student object (already added to the database)

    Creates the student with the passed in paramaters and returns it.
    """

    new_student = User(fname = fname, lname = lname, email = email, osis = osis)
    new_student.set_password(password)
    new_student.add_role('student')

    db.session.add(new_student)
    db.session.commit()

    return new_student
