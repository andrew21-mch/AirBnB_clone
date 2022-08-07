#!/usr/bin/python3

"""
User model
"""

# class user that inherits from BaseModel
from models.base_model import BaseModel


class User(BaseModel):
    # public class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    """
    Class User
    """
    pass

