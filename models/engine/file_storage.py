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


