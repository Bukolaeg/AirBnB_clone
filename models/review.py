#!/usr/bin/python3
"""
Created on: Dec. 06, 2023
@authors: Bukola Egberongbe
          Jamiu Olukayode Shomoye
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel

    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method for Review class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
