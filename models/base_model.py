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
    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes
        """
        """Verificamos que no llegue vacio"""
        if len(kwargs) > 0 and kwargs is not None:
            """Recorremos los valores que llegan"""
            for llave, valor in kwargs.items():
                """Para configurar la hora verificamos el nombre de la llave"""
                if llave == "created_at" or llave == "updated_at":
                    """strptime:crea un objeto de fecha y hora a partir de la cadena dada, 1 parametro: la cadena a convertir, 2 el formato"""
                    valor = datetime.strptime(valor, '%Y-%m-%dT%H:%M:%S.%f')
                """Observe que __class__ de kwargs es el único que no debe añadirse como atributo."""    
                if llave != "__class__":
                    """La función setattr() establece el valor del atributo de un objeto."""
                    setattr(self, llave, valor)
        else:
            """si no cree id y created_at como lo hizo anteriormente (nueva instancia)"""
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
