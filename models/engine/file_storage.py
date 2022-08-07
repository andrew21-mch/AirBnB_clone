#!/usr/bin/python3

"""
File storage engine
"""

# pylint:disable=invalid-name, unused-argument
# pylint:disable=attribute-defined-outside-init

import json
from datetime import datetime
from models.base_model import BaseModel

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
MODELS = [BaseModel]


class FileStorage:
    """
    class implementation of file storage
    """

    __file_path: str = 'file.json'
    __objects: dict = {}

    # def __init__(self):
    #     """
    #     constructor
    #     """
    #     # super().__init__()
    #     pass

    def all(self):
        """
        :returns: the dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        :param obj: instance
        sets in __objects the obj with ket <obj classname>.id
        """
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to json (in __file_path)
        """
        # print(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump({k: v.to_dict() for k, v in
                       FileStorage.__objects.items()}, json_file, indent=4)

        # because save() overwrites __dict__ as to_dict(), \
        # reconvert the datetime str to obj and \
        # remove __class__
        for k, v in FileStorage.__objects.items():
            for ck, cv in v.__dict__.items():
                if ck in ('created_at', 'updated_at'):
                    v.__dict__[ck] = datetime.strptime(cv, DATE_FORMAT)
            # v.__dict__.__delitem__('__class__') use del or pop instead
            v.__dict__.pop('__class__')

    def reload(self):
        """
        deserializes the json file to __objs
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') \
                    as json_file:
                dict_objs = json.load(json_file)

            if dict_objs:
                for k, v in dict_objs.items():
                    # destructure the key to model name and object id
                    # but use only model name
                    class_name = k.split('.')[0]
                    for class_model in MODELS:
                        if class_model.__name__ == class_name:
                            obj = class_model(**v)
                            self.new(obj)

        except FileNotFoundError:
            pass

    def find(self, model: str, inst_id: str, should_delete: bool = False):
        """
        find instance of model wih given id
        """

        all_objs = self.all()
        model_class = None
        instance = None
        selected_header = None
        for header, obj in all_objs.items():
            model_name, obj_id = header.split(".")
            if model_name == model:
                # print('Model found')
                model_class = model_name
                if obj_id == inst_id:
                    # print('Instance found')
                    # instance = obj
                    selected_header = header

                else:
                    # print('Instance not found')
                    continue
            else:
                # print('Model not found')
                continue

        if selected_header:
            if should_delete:
                instance = all_objs.pop(selected_header)
                self.save()
            else:
                instance = all_objs.get(selected_header)
        return model_class, instance

    def delete(self, model, inst_id):
        """
         delete instance
        """
        # all_objs = self.all()
        # model_class = None
        # instance = None
        # key_to_pop = None  # popping during loop changes size
        # for header, obj in all_objs.items():
        #     model_name, obj_id = header.split(".")
        #     if model_name == model:
        #         # print('Model found')
        #         model_class = model_name
        #         if obj_id == inst_id:
        #             # print('Instance found')
        #             # instance = obj
        #             # instance = all_objs.pop(header)
        #             key_to_pop = header
        #
        #         else:
        #             # print('Instance not found')
        #             continue
        #     else:
        #         # print('Model not found')
        #         continue
        # if key_to_pop:
        #     instance = all_objs.pop(key_to_pop)
        # return model_class, instance

        return self.find(model, inst_id, True)