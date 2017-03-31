""" Provides helpers for testing the models

create_user() -- returns the created user object
create_role(role) -- returns the created role object
"""

from app.extensions import db
from app.models.users import User
from app.models.permissions import Role
