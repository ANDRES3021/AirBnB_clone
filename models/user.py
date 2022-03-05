#!/usr/bin/python3
"""modulo que administra la clase usuario"""
from models.base_model import BaseModel


class User(BaseModel):
    """Clase que representa usuario"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Función para crear una nueva instancia"""
        super().__init__(*args, **kwargs)
