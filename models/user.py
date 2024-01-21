#!/usr/bin/python3
"""
Model for the user class   
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    class User that handles user's information
    Args:
        BaseModel (_type_): _description_
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
