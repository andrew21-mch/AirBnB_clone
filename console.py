#!/usr/bin/python3

"""
console
"""

# pylint:disable=broad-except, unused-argument, invalid-name


import cmd
import re

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


MODELS = [BaseModel, User, State, City, Amenity, Place, Review,]


class HBNBCommand(cmd.Cmd):
    """
    hbnb CLI implementation
    """

    prompt = '(hbnb) '

    def str_to_class(self, model: str):
        """
        :return: class obj from str
        """
        class_obj = None
        try:
            if globals()[model]:
                class_obj = globals()[model]
        except Exception:
            pass
        return class_obj

    def do_quit(self, line):
        """
        quit console
        """
        return True

    def do_EOF(self, line):
        """
        quit console on EOF
        """
        return True

    def check_input(self, line):
        """
        checks if input exist
        """
        has_input = False
        if line == "":
            print('** no_class')
        else:
            has_input = True
        return has_input

    def parse(self, line: str, arg_len: int, should_delete: bool = False):
        """
        handler for one input operations
        """
        has_input = self.check_input(line) #boolean to check input

        argv = line.split(" ")
        argc = len(argv)
        # too_many_args = False

        if arg_len == 1: # one input handling
            model_class = None  # avoid unpack error
            if has_input: #if there is and input and count is 1
                if argc == 1:
                    model_class = self.str_to_class(argv[0])
                    # return model_class
                else:
                    print('** too_many arguments passed')
            return model_class

        elif arg_len == 2:
            # two inputs
            # model and id
            model_class = None
            instance = None

            if has_input:
                if argc == 2:
                    model_name, obj_id = argv
                    model_class, instance = models.storage.find(model_name, obj_id, should_delete)
                    # print(model_class, instance)

                    if model_class is None:
                        print('** invalid_class')
                    elif instance is None:
                        print('** invalid_id')
                    # else:
                    #     # print(str(instance))
                    #     return model_class, instance

                elif argc == 1:
                    print('** no_id')

                else:
                    print('** too_many args passed')
            return model_class, instance

        elif arg_len == 4:
            # four inputs
            # model, id, attribute, value
            model_class = instance = attrib = value = None

            if has_input:
                if argc == 1:
                    print('** no_id')
                elif argc == 2:
                    print('** no_attrib')
                elif argc == 3:
                    print('** no_value')
                else:
                    model_name, obj_id, attrib, value = argv[:4]
                    model_class, instance = models.storage.find(model_name, obj_id, should_delete)
                    if model_class is None:
                        print('** invalid_class')
                    elif instance is None:
                        print('** invalid_id')
            return model_class, instance, attrib, value

        else:
            print('** ** Accepted values are 1, 2 and 4 **')

    def do_create(self, line):
        """
        Creates an instance from the valid model argument
        """

        model_class = self.parse(line, 1)
        if model_class:
            obj = model_class()
            models.storage.new(obj)
            obj.save()

    def do_show(self, line: str):
        """
        Show instance of model with specified id
        """
        instance = self.parse(line, 2)
        if instance:
            print(str(instance))

    # def do_destroy(self, line):
    #     """
    #     Deletes an instance based on the class name and id
    #     """
    #     model_class, instance = self.parse(line, 2, True)
    #     # if instance:
    #     #     print(f"** {instance.id} destroyed **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        array = []
        if line == "":
            for header, obj in models.storage.all().items():
                array.append(str(obj))
        else:
            model_class = self.parse(line, 1)
            if model_class:
                for header, obj in models.storage.all().items():
                    if header.split(".")[0] == model_class.__name__:
                        array.append(str(obj))
            else:
                print('** invalid_class')

        if array:
            print(array)

    def do_update(self, line):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute
        """

        model_class, instance, attrib, value = self.parse(line, 4)
        if instance and attrib and value:
            str_pat = r"^\"[\S]+\"$"
            value_is_str = re.match(str_pat, value)
            adjusted_value = None

            if value_is_str:
                adjusted_value = value_is_str.group().replace("\"", "")
            else:
                try:
                    adjusted_value = int(value)
                except ValueError:
                    try:
                        adjusted_value = float(value)
                    except ValueError:
                        print("** Invalid value format for attribute **")

            if adjusted_value:
                setattr(instance, attrib, adjusted_value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()