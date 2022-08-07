#!/usr/bin/python3

"""
User model
"""

# class user that inherits from BaseModel
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    # public class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__ = User
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def __str__(self):
        return "[User] ({}) {}".format(self.id, self.__dict__)
        

