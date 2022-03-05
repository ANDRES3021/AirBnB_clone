#!/usr/bin/python3
"""
Modulo de la clase State que hereda de BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Clase State que contiene el atributo name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
