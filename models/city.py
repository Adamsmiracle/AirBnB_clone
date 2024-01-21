#!/usr/bin/python3
"""
module for city
"""

from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """

    Args:
        BaseModel (class): _base class_
        Attributes:
            name (str): name of the city
            state_id (str): state that the city belongs to
    """
    
    name = ""
    state_id = ""