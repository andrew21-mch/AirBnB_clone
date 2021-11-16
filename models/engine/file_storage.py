class FileStorage:
    """
    Serilaizes instance to JSON file and deserializes
    JSON files to instances.
    Private class attributes:
        @__file_path: string - path to the JSON file (ex: file.json)
        @__objects: dictionary - empty but will store all objects by
                    <class name>.id (ex: to store a BaseModel object
                with id=12121212, the key will be BaseModel.12121212)
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON
                      file (__file_path) exists ; otherwise, do nothing. If the
                      file doesn’t exist, no exception should be raised)
    """

    #private instance attributes
    __file_path = "file.json"
    __objects = {}

    #public instance methods
    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the json file at __file_path"""
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception is raised)
        """

        try:
            with open(FileStorage.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for obj_str in obj_dict.values():
                    cls = eval(obj_str["__class__"])
                    new_obj = cls(**obj_str)
                    self.new(new_obj)

        except FileNotFoundError:
            pass
