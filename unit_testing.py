import unittest
from test import add

class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(add(4,4), 8)
        
    def test_function2(self):
        self.assertEqual(add(5,4), 4)
        
if __name__ == '__main__':
    unittest.main()