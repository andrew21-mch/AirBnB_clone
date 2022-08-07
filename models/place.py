# class place

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    """
    # public class attributes
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__ = Place
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])

    def __str__(self):
        return "[Place] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """
        Returns the dictionary representation of a Place instance
        """
        new_dict = super().to_dict()
        new_dict['city_id'] = self.city_id
        new_dict['user_id'] = self.user_id
        new_dict['name'] = self.name
        new_dict['description'] = self.description
        new_dict['number_rooms'] = self.number_rooms
        new_dict['number_bathrooms'] = self.number_bathrooms
        new_dict['max_guest'] = self.max_guest
        new_dict['price_by_night'] = self.price_by_night
        new_dict['latitude'] = self.latitude
        new_dict['longitude'] = self.longitude
        new_dict['amenity_ids'] = self.amenity_ids
        return new_dict
        