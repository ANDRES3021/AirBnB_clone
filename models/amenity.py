#!/usr/bin/python3
"""
Modulo de la clase Amenity que hereda de BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Clase Amenity que contiene el atributo name.
    """
    name = ""

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
