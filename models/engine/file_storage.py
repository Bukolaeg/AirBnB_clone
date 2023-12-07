#!/usr/bin/env python3
"""
Created on: Dec. 06, 2023
Authors: Bukola Egberongbe
         Jamiu Olukayode Shomoye
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    FileStorage - a BaseModel that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path (str) - path to the JSON fil
        __objects (dict) - to store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all - returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new - sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj (Python object): The object to set
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save - serializes __objects to a JSON file (path: __file_path)
        """
        file_dict = {key: value.to_dict() for key, value in
                     FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(file_dict, file)

    def reload(self):
        """
        reload - deserializes a JSON file to __objects only if the JASON file
        exists, otherwise raise an exceltion that does nothing but return.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json_file = json.load(file)
            for k, v in json_file.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except:
            pass
