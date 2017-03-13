""" Tests the users.py file

Checks get_user(id)
"""

from app.models.users import get_user

def test_get_user():
    assert None == get_user(0)
