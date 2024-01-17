import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    class for storing the objects
    """
    __file_path = "file.json"
    
    __objects = {}
    
    def new(self, obj):
        """
        saves an instance to the __object dictionary

        Args:
            obj (_object_): _for saving data when an instance is created_
        """
        object_class_name = obj.__class__.__name__
        key = "{}.{}".format(object_class_name, obj.id)
        FileStorage.__objects[key] = obj
        
    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_objects = FileStorage.__objects
        object_dictionary = {}
        
        for obj in all_objects.keys():
            object_dictionary[obj] = all_objects[obj].to_dict()
            
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dictionary, file)
            
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dictionary = json.loads(file)
                
                    for key, value in object_dictionary.items():
                        class_name, object_id = key.split(".")
                        
                        cls = eval(class_name)
                        
                        instance = cls(**value)
                        
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass