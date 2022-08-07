#!/usr/bin/python3

"""
City model
"""
class City:
    """
    City class
    """
    # public class attributes
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__ = City
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
    def __str__(self):
        return "[State] ({}) {}".format(self.id, self.__dict__)
    
