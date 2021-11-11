import uuid
from datetime import datetime


class BaseModel:
    """ this mwill be models contains attributes that and methods """
    id = str(uuid.uuid4())
    created_at = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')
    updated_at = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')


    def __str__(self):
        return f'{self.__class__.__name__} {self.id}  {self.__dict__}'
