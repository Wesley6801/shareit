import booksAPI as booksrunAPI
from util.db_utils import *
from util.auth_utils import *
import unittest
import sys

sys.path.append('../shareit')
test_isbn = 9781284140996
response_correct = booksrunAPI.get_bookPrices_json(test_isbn)
response_incorrect = booksrunAPI.get_bookPrices_json("wrong")


class TestPages(unittest.TestCase):

    def test_json(self):
        d = type(response_correct)
        self.assertEqual(d, dict)

    def test_json_wrong_isbn(self):
        self.assertEqual(response_incorrect, "Error")
        response = booksrunAPI.get_bookPrices_json(booksrunAPI)
        self.assertEqual(response, "Error")

    def test_string(self):
        response = booksrunAPI.get_bookPrices(
            "Java Illuminated", response_correct)
        self.assertNotEqual(response, "Error")

    def test_string_wrong_isbn(self):
        response = booksrunAPI.get_bookPrices(
            "Don't exist", response_incorrect)
        self.assertEqual(response, "Error")
        response = booksrunAPI.get_bookPrices("Don't exist", booksrunAPI)
        self.assertEqual(response, "Error")


if __name__ == "__main__":
    unittest.main()
