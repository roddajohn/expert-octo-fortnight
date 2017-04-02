""" Tests the permissions.py file

Tests the __repr__ function
All other methods are tested through app.models.users.User methods (add_role, remove_role, etc)
"""

from app.extensions import db
from app.models.permissions import Role
from tests.models.helpers import create_test_role

def test_repr():
    """ Tests the __repr__ """

    r = create_test_role()
    db.session.add(r)
    db.session.commit()

    assert str(r) == '<Role ID: %d>' % r.id
