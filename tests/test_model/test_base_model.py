#!/usr/bin/python3
"""
This is the test for the base model class
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """_summary_

    Args:
        unittest (model): _for testing the class_
    """
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        test for the save function
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        test for the dict class
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"],
                        my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"],
                        my_model.updated_at.isoformat())

    def test_str(self):
        """
        test for the string representation class
        """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("['BaseModel']"))
        
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))