import unittest
import sys

sys.path.append("../")
from main import *

class test_pages(unittest.TestCase):
    
    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_register(self):
        pass
    
    def test_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code,200 )