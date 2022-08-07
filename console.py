#!/usr/bin/python3

"""
console
"""



import cmd

from models.base_model import BaseModel

MODELS = [BaseModel]


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
        Quit command to exit the program 
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()