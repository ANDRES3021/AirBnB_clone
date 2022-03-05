#!/usr/bin/python3
"""
Modulo de la clase Review que hereda de BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Clase Review que contiene varios atributos.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
