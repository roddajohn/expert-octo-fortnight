""" Tests the users.py file 
"""

import pytest

from app.models.users import User

def test_insert():
    """ Tests the User insert method """

    new = User('testing@testing.com')

    # THIS IS NOT DONE

