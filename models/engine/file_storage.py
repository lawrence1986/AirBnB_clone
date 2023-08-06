#!/usr/bin/python3
"""This is the Module for class FileStorage"""
import datetime
import json
import os

class FileStorage:
    """File path to store data"""

    __file_path = "folder.json"
    
    """Dictionary to store objects"""
    __objects = {}

    def all(self):
        """This returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Generates a key for the object,adds it to objects dict"""
        class_name = type(obj).__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects dictionary to a JSON file"""
        fso = FileStorage.__objects
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in fso.items()}
            json.dump(d, f)

    def reload(self):
        """Reloads the objects dictionary from the JSON file"""
        file_path = FileStorage.__file_path

        if not os.path.isfile(file_path):
            return
        with open(file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
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

    def attributes(self):
        """Defines attributes and their types for each class"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
