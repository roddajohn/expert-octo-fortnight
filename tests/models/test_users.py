""" Tests the users.py file

Checks get_user(id)
Check add_user(user_data)
"""

from app.models.users import get_user, add_user

def test_add_user():
    assert not 0 == add_user({'username': 'johnrodjohn'})

def test_get_user():
    assert None == get_user(0)
