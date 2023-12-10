#!/usr/bin/python3
"""
Created on: Dec. 06, 2023
@authors: Bukola Egberongbe
          Jamiu Olukayode Shomoye
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel

    Attribute:
        name (str): Public class attribute for Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for Amenity class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
