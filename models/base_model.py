#!/usr/bin/python3
"""This script is basically the Base Model"""

import uuid
import datetime
from models import storage


class BaseModel:

    """The Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """This Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            self.load_attributes(**kwargs)
        else:
            self.initialize_attributes()
            storage.new(self)

    def load_attributes(self, **kwargs):
        """This Loads instance attributes from key-value pairs"""

        for key, value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
            if key != "__class__":
                setattr(self, key, value)

    def initialize_attributes(self):
        """This Initializes instance attributes if no kwargs provided"""

        self.id = str(uuid.uuid4())
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        """Simply Returns official string representation"""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
