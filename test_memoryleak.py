# test_memoryleak.py
"""
Tests for MemoryLeak module.
"""

import unittest
from memoryleak import MemoryLeak

class TestMemoryLeak(unittest.TestCase):
    """Test cases for MemoryLeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MemoryLeak()
        self.assertIsInstance(instance, MemoryLeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MemoryLeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
