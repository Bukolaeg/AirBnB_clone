#!/usr/bin/python3
"""
Created on: Dec. 06, 2023
@authors: Bukola Egberongbe
          Jamiu Olukayode Shomoye
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel

    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
