import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
    Testing the instantiation  of file storage

    Args:
        unittest (_type_): _description_
    """
    
    def test_FileStorage_instantiation_no_args(self):
        # Test creating a FileStorage instance with no arguments
        self.assertEqual(type(FileStorage()), FileStorage)
        
    def test_FileStorage_instantiation_with_args(self):
        #test creating a Filestorage instance with an argument
        #should raise tyepError
        with self.assertRaises(TypeError):
            FileStorage(None)
            
    def test_storage_initializes(self):
        # test if the storage  variable in models is an instance of filestorage.
        self.assertEqual(type(models.storage), FileStorage)
        
class TestFileStorage(unittest.TestCase):
    def setUp(self):
        #create a temporary test file for saving data
        self.test_file = "test_file.json"
        
    def tearDown(self):
        #remove the temporary test file after teh test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def test_all_storage_returns_dictionary(self):
        #test if the all method returns dictionary
        self.assertEqual(dict, type(models.storage.all()))
        
    def test_new(self):
        #test teh new method by creating and storing a new object
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())
        
        
    def test_new_with_args(self):
        #test creating a new object with additional arguements
        # (should raise TypeError)
        with self.assertRaises(TypeError):
            models.storage.new(self,BaseModel())
            
    def test_new_with_None(self):
        #test creating a newe object with None (should raise attributeError)
        with self.assertRaises(AttributeError):
            models.storage.new(None)
            
if __name__=="__main__":
    unittest.main()