def help_create(self):
    """
        prints Help info for the create function
    """
    print("""Creats a new instance of the first argument
          stores it in the JSON file and prints its id""")

def do_show(self, arg):
    """
        Prints the string representation of an instance based
        on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
    """
    arg_lst = HBNBCommand.parse(arg)
    db = storage.all()
    if not len(arg_lst):
        print("** class name missing **")
    elif (arg_lst[0] not in HBNBCommand.__class_lst.keys()):
        print("** class doesn't exist **")
    elif len(arg_lst) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in db:
        print("** no instance found **")
    else:
        print(db["{}.{}".format(arg_lst[0], arg_lst[1])])

    # Extra case
    # elif len(arg_lst) > 2:
    #    print("** to many arguments **")

def help_show(self):
    """
        Prints Help for for the creat function
    """
    print("""Prints the string representation of an instance based
        on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """)

def do_destroy(self, arg):
    """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234
    """
    arg_lst = HBNBCommand.parse(arg)
    storage.reload()
    db = storage.all()
    if not len(arg_lst):
        print("** class name missing **")
    elif (arg_lst[0] not in HBNBCommand.__class_lst.keys()):
        print("** class doesn't exist **")
    elif len(arg_lst) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in db:
        print("** no instance found **")
    else:
        # print(storage.__class__.__name__.__objects)
        del db["{}.{}".format(arg_lst[0], arg_lst[1])]
        storage.save()

def help_destroy(self):
    """
        Prints Help for the destroy function
    """
    print("""Deletes an instance based on the class name and id
          (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234""")

def do_all(self, arg):
    """
        Prints all string representation of all instances based or
        not on the class name.
            Ex: $ all BaseModel or $ all
    """
    arg_list = HBNBCommand.parse(arg)
    if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
        print("** class doesn't exist **")
    else:
        objl = []
        for obj in storage.all().values():
            if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                objl.append(obj.__str__())
            elif len(arg_list) == 0:
                objl.append(obj.__str__())
        print(objl)

def help_all(self):
    """
        prints help for the all function
    """
    print("""Prints all string representation of all instances based or
        not on the class name.
            Ex: $ all BaseModel or $ all""")

def do_update(self, arg):
    """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email
                  "aibnb@holbertonschool.com"
    """
    arg_list = HBNBCommand.parse(arg)
    objdict = storage.all()

    if len(arg_list) == 0:
        print("** class name missing **")
        return False
    if arg_list[0] not in HBNBCommand.__class_lst:
        print("** class doesn't exist **")
        return False
    if len(arg_list) == 1:
        print("** instance id missing **")
        return False
    if "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
        print("** no instance found **")
        return False
    if len(arg_list) == 2:
        print("** attribute name missing **")
        return False
    if len(arg_list) == 3:
        try:
            type(eval(arg_list[2])) != dict
        except NameError:
            print("** value missing **")
            return False
    if len(arg_list) == 4:
        obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
        if arg_list[2] in obj.__class__.__dict__.keys():
            valtype = type(obj.__class__.__dict__[arg_list[2]])
            obj.__dict__[arg_list[2]] = valtype(arg_list[3])
        else:
            obj.__dict__[arg_list[2]] = arg_list[3]
    elif type(eval(arg_list[2])) == dict:
        obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
        for k, v in eval(arg_list[2]).items():
            if (k in obj.__class__.__dict__.keys() and type(
                    obj.__class__.__dict__[k]) in {str, int, float}):
                valtype = type(obj.__class__.__dict__[k])
                obj.__dict__[k] = valtype(v)
            else:
                obj.__dict__[k] = v
    storage.save()

def help_update(self):
    """
        prints Help for the update function
    """
    print(
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234
                  email "aibnb@holbertonschool.com""")

def emptyline(self):
    """
        Does nothing if Empty line + enter is inserted.
        Used for overriding the emptyline function
    """
    pass

def do_count(self, arg):
    """
        Prnits the number of elements inside the FileStorage that
        are of instances of cls
    """
    arg_list = HBNBCommand.parse(arg)
    if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
        print("** class doesn't exist **")
    else:
        objl = []
        for obj in storage.all().values():
            if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                objl.append(obj.__str__())
            elif len(arg_list) == 0:
                objl.append(obj.__str__())
        print(len(objl))

def show(self, cls):
    """
        Gives all the elements inside the FileStorage that
        are of instances of cls
    """
    pass

def destroy(self, cls):
    """
        Gives all the elements inside the FileStorage that
        are of instances of cls
    """
    pass

def update(self, cls):
    """
        Gives all the elements inside the FileStorage that
        are of instances of cls
    """
    pass

def default(self, line):
    """
        Handles the case where the the command has no equivlaent
        do_ method
    """

    line_p = HBNBCommand.parse(line, '.')
    if line_p[0] in HBNBCommand.__class_lst.keys() and len(line_p) > 1:
        if line_p[1][:-2] in HBNBCommand.__class_funcs:
            func = line_p[1][:-2]
            cls = HBNBCommand.__class_lst[line_p[0]]
            eval("self.do_" + func)(cls.__name__)
        else:
            print("** class doesn't exist **")
    else:
        super().default(line)
    return False
