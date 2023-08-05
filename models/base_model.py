#!/usr/bin/python3
"""Basemodel script"""


import uuid
import datetime
from models import store



class BaseModel:

    def __init__(self, *ptr, **kwptr):
        if kwptr != None and kwptr != {}:
            for entry in kwptr:
                if entry == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwptr["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif entry == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwptr["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[entry] = kwptr[entry]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def __str__(self):
        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now()
        store.save()

    def to_dict(self):

        is_dict = self.__dict__.copy()
       is_dict["__class__"] = type(self).__name__
        is_dict["created_at"] = is_dict["created_at"].isoformat()
        is_dict["updated_at"] = is_dict["updated_at"].isoformat()
        return is_dict

