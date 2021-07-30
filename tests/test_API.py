import booksrunAPI
import main
import unittest
import sys

sys.path.append('../shareit')
from util.auth_utils import *
from util.db_utils import *
test_isbn = 9781284140996


class TestPages(unittest.TestCase):

    def test_json(self):
        response = booksrunAPI.get_bookPrices_json(test_isbn)
        d = type(response)
        self.assertEqual(d, dict)

    def test_json_wrong_isbn(self):
        response = booksrunAPI.get_bookPrices_json("wrong")
        self.assertEqual(response, "Error")
        response = booksrunAPI.get_bookPrices_json(booksrunAPI)
        self.assertEqual(response, "Error")

    def test_string(self):
        response = booksrunAPI.get_bookPrices("Java Illuminated", test_isbn)
        self.assertNotEqual(response, "Error")

    def test_string_wrong_isbn(self):
        response = booksrunAPI.get_bookPrices("Don't exist", "wrong")
        self.assertEqual(response, "Error")
        response = booksrunAPI.get_bookPrices("Don't exist", booksrunAPI)
        self.assertEqual(response, "Error")

        

if __name__ == "__main__":
    unittest.main()
