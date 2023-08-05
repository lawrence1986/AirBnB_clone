#!/usr/bin/python3

import datetime
import json
import os



class FileStorage:

    __file_path = "folder.json"
    __objects = {}

    def all(self):

        return FileStorage.__objects

    def new(self, obj):

        class_name = type(obj).__name__
        key = "{}.{}".format(class_name, obj.id)
        obj = FileStorage.__objects[key]

    def save(self):

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        file_path = FileStorage.__file_path

        if not os.path.isfile(file_path):
            return
        with open(file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            obj_dict = FileStorage.__objects

    def classes(self):

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
