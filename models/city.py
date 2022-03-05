#!/usr/bin/python3
"""
Modulo de la clase City que hereda de BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Clase City que contiene el atributo name y state_id.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
