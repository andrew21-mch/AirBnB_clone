import uuid
from datetime import datetime


class BaseModel:
    """ this mwill be models contains attributes that and methods """
    id = str(uuid.uuid4())
    created_at = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')
    updated_at = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')


    def __str__(self):
        """ String representation"""
        return f'{self.__class__.__name__} {self.id}  {self.__dict__}'

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.updated_at


    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        to_dict = dict(self.__dict__)
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        to_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return to_dict
