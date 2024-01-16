#!/usr/bin/python3
"""
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs:
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        
        return inst_dict
    
    def __str__(self):
        """
        Returns string representation of the instance
        """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
    
    
if __name__ == "__main__":
    model = BaseModel()
    model.name = "My first model"
    model.my_number = 90
    print(model)
    model.save()
    print(model)
    model_json = model.to_dict()
    print(model_json)
    print("JSON of my model")
    for key in model_json:
        print(f"\t{key}: ({type(model_json[key])}) - {model_json[key]}")