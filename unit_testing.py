import unittest
from test import convert_to_json, specifc_new_story_url
from test import new_url_to_json, create_table, export_to_mysql 

class TestFileName(unittest.TestCase):
    def test_function1(self):
        url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
        self.assertNotEqual(convert_to_json(url), " ")
        
    def test_function2(self):
        url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
        self.assertNotEqual(specifc_new_story_url(url), "")
    def test_function3(self):
    
    def test_function4(self):
      
    def test_function5(self):
        
if __name__ == '__main__':
    unittest.main()