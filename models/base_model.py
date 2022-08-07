#!/usr/bin/python3

"""
BaseModel module
"""

# pylint:disable=invalid-name, unused-argument
# pylint:disable=attribute-defined-outside-init

from uuid import uuid4
from datetime import datetime

import models
# from models import storage



class BaseModel:
    """
    Class BaseModel
    """
    # __dict__ = {}

    def __init__(self, *args, **kwargs):
        """
        :param args: not used
        :param kwargs: instance data
        """
        if kwargs:
            # attrs = {}
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ('created_at', 'updated_at'):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    # setattr(self, k, v)

                setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        :return: store instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        :return: dict repr of instance
        """
        dict_obj = self.__dict__
        for k, v in dict_obj.items():
            if k in ("created_at", "updated_at"):
                dict_obj[k] = v.isoformat()

        dict_obj['__class__'] = type(self).__name__
        return dict_obj


if __name__ == "__main__":


    all_objs = models.storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)