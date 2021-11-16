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


    def __str__(self):
        """ String representation"""
        return f'{self.__class__.__name__} {self.id}  {self.__dict__}'

    def save(self):
        """
        updates the updated_at public instance variable
        """

        self.updated_at = datetime.today()
        models.storage.save()



    def to_dict(self):
        def to_dict(self):
        """
            return the dictionary representation of the object to_dict
        """

        obj_repr = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                obj_repr[key] = value.isoformat()
            else:
                obj_repr[key] = value

        obj_repr["__class__"] = self.__class__.__name__

        return obj_repr
