""" Convenience functions which interact with SQLAlchemy models. """

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr, declarative_base

from app.extensions import db

class Base(db.Model):
    """Convenience base DB model class. Makes sure tables in MySQL are created as InnoDB.

    This is to enforce foreign key constraints (MyISAM doesn't support constraints) outside of production. Tables are also named to avoid collisions.
    """

    @declared_attr
    def __tablename__(self):
        return '{}'.format(self.__name__.lower())

    __abstract__ = True
    __table_args__ = dict(mysql_charset='utf8', mysql_engine='InnoDB')
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    """ Primary key for SQL Alchemy models. """
