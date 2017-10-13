""" Tests app.core.students """

import pytest

from app.core.students import create_student

from app.models.users import User

def test_create_student():
    """ Tests the create_student method """

    student = create_student('test_fname', 'test_lname', 'test_password', 'test_email', 0)

    assert student.fname == 'test_fname'
    assert student.lname == 'test_lname'
    assert student.check_password('test_password')
    assert student.email == 'test_email'
    assert student.osis == 0
    assert User.query.filter_by(id = student.id).first() == student
