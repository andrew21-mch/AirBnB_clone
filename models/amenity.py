#!/usr/bin/python3

"""
Amnety model
"""

class Amenity:
    """
    Amnety class
    """
    # public class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        self.__class__ = Amenity
        self.name = kwargs.get('name', '')
    def __str__(self):
        return "[Amnety] ({}) {}".format(self.id, self.__dict__)
    
