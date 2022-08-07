#!/usr/bin/python3

"""
Review model
"""

class Review:
    """
    Review class
    """
    # public class attributes
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__ = Review
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')
