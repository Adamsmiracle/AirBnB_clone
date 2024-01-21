#!/usr/bin/python3
"""
model for state data
"""

from models.base_model import BaseModel

class State(BaseModel):
    """

    Args:
        BaseModel (class): The base model class
    
    Attributes:
        name (str): name of the state
    """
    name = ""