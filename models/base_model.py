#!/usr/bin/python3
"""
Clase que define el modulo base
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    Como su nombre lo indica es la clase base de este proyecto y su funcion es contener tanto los atributos y metodos comunes de otras clases.
    """
    def __init__(self):
        """Initialize the instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at =  datetime.now()

    def __str__(self):
        """Cancela el comportamiento normal de __str__"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Actualiza el atributo update con la hora y fecha actual"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returna un diccionario con todas las clases/valor de la instancia"""
        dictionary = self.__dict__
        dictionary.update({"__class__": type(self).__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return dictionary
