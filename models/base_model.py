#!/usr/bin/python3
"""
    A base model class for all the
    classes to be created in the airbnb module. This class
    will define all the basic things (attributes and functions)
    that will be used through out the project by other class
    as well
"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """A base for all the classes in the AirBnb console application
    Atrributes:
        @id: string - assign with a uuid when an instance is created:
        @created_at: datetime - assign with the current datetime when
                     an instance is created
        @updated_at: datetime - assign with the current datetime when
                     an instance is created and it will be updated every
                     time you object is modified or changed
    Methods:
        @__str__: should print: [<class name>] (<self.id>) <self.__dict__>
        @save(self): updates the public instance attribute updated_at with
                     the current datetime
        @to_dict(self): returns a dictionary containing all keys/values of
                        __dict__ of the instance:
            - by using self.__dict__, only instance attributes set will be
              returned
            - a key __class__ must be added to this dictionary with the class
              name of the object
            - created_at and updated_at must be converted to string object in
              ISO format:
                - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
    """
    id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            models.storage.new(self)

    def __str__(self):
        """ String representation"""
        return self.__class__.__name__, self.id,\
        self.__dict__.__format__("{:s} {:s} {}")

    def save(self):
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        to_dict = dict(self.__dict__)
        to_dict['__class__'] = self.__class__.__name__
        to_dict['updated_at'] = self.updated_at\
        .strftime("%Y-%m-%dT%H:%M:%S.%f")
        to_dict['created_at'] = self.created_at\
        .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return to_dict
