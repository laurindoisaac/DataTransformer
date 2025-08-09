# test_datatransformer.py
"""
Tests for DataTransformer module.
"""

import unittest
from datatransformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    """Test cases for DataTransformer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataTransformer()
        self.assertIsInstance(instance, DataTransformer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataTransformer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
