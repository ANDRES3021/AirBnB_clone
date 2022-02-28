#!/usr/bin/python3
import datetime
import uuid


class BaseModel():
    def __init__(self):
        """Initialize the instance attributes
        """
        self.id = uuid.uuid4
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary.update({"__class__": self.__class__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return dictionary
