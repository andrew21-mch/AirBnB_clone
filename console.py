#!/usr/bin/python3

"""
console
"""

# pylint:disable=broad-except, unused-argument, invalid-name


import cmd
import re

import models
from models.base_model import BaseModel

MODELS = [BaseModel]


class HBNBCommand(cmd.Cmd):
    """
    hbnb CLI implementation
    """

    prompt = '(hbnb) '

    ERROR_MSGS = {
        "no_class": "** class name missing **",
        "invalid_class": "** class doesn't exist **",
        "no_id": "** instance id missing **",
        "invalid_id": "** no instance found **",
        "too_many": "** too many arguments **",
        "no_attrib": "** attribute name missing **",
        "no_value": "** value missing **"
    }

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()