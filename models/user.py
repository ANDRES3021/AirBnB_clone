#!/usr/bin/python3
"""
modulo que administra la clase usuario
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    clase que representa usuario
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
