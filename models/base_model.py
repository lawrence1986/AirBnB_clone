#!/usr/bin/python3
"""Basemodel script"""

import uuid
import datetime
from models import storage


class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """String Representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
			self.__dict__)

    def save(self):
        """This updates the instance updated_at"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""
        is_dict = self.__dict__.copy()
        is_dict["__class__"] = type(self).__name__
        is_dict["created_at"] = is_dict["created_at"].isoformat()
        is_dict["updated_at"] = is_dict["updated_at"].isoformat()
        return is_dict
