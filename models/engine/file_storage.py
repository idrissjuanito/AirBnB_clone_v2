#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects
        cls_objects = {}
        for key in FileStorage.__objects.keys():
            if cls in key:
                cls_objects[key] = FileStorage.__objects[key]
        return cls_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
                {obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """deletes an object from the __objects """
        if not obj:
            return
        try:
            key = obj.to_dict()['__class__']+'.'+obj.id
            del FileStorage.__objects[key]
        except KeyError:
            return

    def reload(self):
        """Loads storage dictionary from file"""
        from os import getenv
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = {"User": User, "BaseModel": BaseModel,
                   "Place": Place, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Review": Review}
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    item = classes[val['__class__']](**val)
                    self.__objects[key] = item
        except FileNotFoundError:
            pass

    def close(self):
        """ calls reload method """
        self.reload()
