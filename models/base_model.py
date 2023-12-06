#!/usr/bin/env python3
"""
Created on: Dec. 06, 2023
Authors: Bukola Egberongbe
         Jamiu Olukayode Shomoye
"""
from datetime import datetime as dt
import uuid

dt_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel - defines all common attributes/methods for its subclasses.
    """
    def __init__(self, *args, **kwargs):
        """init method for BaseModel Class

        args:
            args (list): list of of aruguments.
            kwargs (dict): key, value arguments dict.

        Attributes:
            id (str) - generated uuid when at instantiiation.
            created_at (datetime): time - current datetime of
            an object instance.
            updated_at (datetime): time - current datetime of
            an update to an object instance.
        """
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = dt.strptime(v, dt_format)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def save(self):
        """
        save - updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = dt.now()

    def to_dict(self):
        """
        to_dict - creates an updated __dict__ containing all keys/values
        of __dict__ and more of the instance

        Return:
            my_dict (dict): Dictionary object that contains
            updated version of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """
        str method for BaseModel Class

        Return:
            string (str): string description for BaseModel Class object
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
