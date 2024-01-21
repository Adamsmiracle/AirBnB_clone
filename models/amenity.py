#!/usr/bin/python3
"""
model for amenity data
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """_summary_

    Args:
        BaseModel (_class_): _base class_
    Attributes:
        name (str): name of the amenity
    """
    name = ""
