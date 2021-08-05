import unittest
import firebase_admin
import pyrebase
import urllib.request
import sys
import os

sys.path.append('../shareit')
from main import *

class test_pages(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_searchAPI(self):
        response = self.app.get('/searchtest', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.app.get('/profile', follow_redirects=True)
        self.assertEqual(response.status_code, 500)

    def test_share(self):
        response = self.app.get('/share', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        response = self.app.get('/checkout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_charge(self):
        response = self.app.get('/charge', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
