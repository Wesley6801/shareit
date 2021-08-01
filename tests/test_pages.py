from main import *
import unittest
import firebase_admin
import pyrebase
import urllib.request
import sys
import os

sys.path.append('/home/codio/workspace/shareit/')


class test_pages(unittest.TestCase):
    #doc = open("../shareit/serviceAccountKey")
    # for items in doc:
    #    print(items)
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        # os.chdir(r'shareit/')
        #file = open('serviceAccountKey.json')
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        # os.chdir(r'shareit/')
        #file = open('serviceAccountKey.json')
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_register(self):
        pass
        # response = self.app.post('/register', data= dict(
        #    name='abc',email='abc@gmail.com',password='abc',confirmed_password='abc',college='abc'))
        #self.assertRedirects(response, '/home')

    def test_login(self):
        # os.chdir(r'shareit/')
        #file = open('serviceAccountKey.json')
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_searchAPI(self):
        # os.chdir(r'shareit/')
        #file = open('serviceAccountKey.json')
        response = self.app.get('/searchtest', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
