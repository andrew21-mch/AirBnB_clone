#!/usr/bin/python3
"""
A console which contains the entry point of the command interpreter:
"""

import cmd

from models import storage
from models.base_model import BaseModel

#other classes when imported goes here

class HBNBCommand(cmd.Cmd):
    """
        HBNBC - a console class for the the airbnb clone
        program
    """

    prompt = '(hbnb) '
    __class_lst = {
        BaseModel.__name__: BaseModel,
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]

    @staticmethod
    def parse(arg, id=" "):
        """
        Returns a list conatning the parsed arguments from the string
        """

        arg_list = arg.split(id)
        narg_list = []

        for x in arg_list:
            if x != '':
                narg_list.append(x)
        return narg_list

    def do_quit(self, arg):
        """Exits the program"""

        return True

    def help_quit(self):
        """Prints help for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints
            the id.
                Ex: $ create BaseModel
        """

        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
            return False

        if len(arg_lst) > 1:
            print("** to many arguments **")
            return False

        if (arg_lst[0] in HBNBCommand.__class_lst.keys()):
            new_obj = HBNBCommand.__class_lst[arg_lst[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
