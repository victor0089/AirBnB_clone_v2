#!/usr/bin/python3
"""Defines the User class victor. """
from models.base_model import BaseModel


class User(BaseModel):
    """RepresentaUser.

    Attributes:
        email (str): Temail of the user.
        password (str): password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
