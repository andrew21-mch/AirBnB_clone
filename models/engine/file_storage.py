#!/usr/bin/python3
""" File Storage"""
import json


class FileStorage:
    """File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ It returns dictionary object"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as write:
            json.dump(self.__objects, write)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        try:
            with open(self.__file_path, 'r') as f:
                json_object = json.load(f)
                return json_object
        except FileExistsError:
            pass
