#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")

        # @hybrid_property
        # def password(self):
        #     """returns the user's password"""
        #     return self._password

        # @password.setter
        # def password(self, value):
        #     """"""
        #     self._password = hashlib.md5(
        #         value.encode('utf8')).hexdigest()
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if "password" in kwargs:
            self._password = hashlib.md5(
                kwargs['password'].encode('utf8')).hexdigest()
        elif "_password" in kwargs:
            self._password = hashlib.md5(
                kwargs['_password'].encode('utf8')).hexdigest()

    @property
    def password(self):
        """returns the user's password"""
        return self._password

    @password.setter
    def password(self, value):
        """set the user's password"""
        self._password = hashlib.md5(
            value.encode('utf8')).hexdigest()
