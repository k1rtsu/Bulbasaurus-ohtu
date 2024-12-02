import unittest
from util import validate_search, UserInputError


class TestSearchTermsValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_search_does_not_raise_error(self):
        search_data = {
                "author": "TestAuthor",
        }
        validate_search(search_data)


    def test_invalid_year_raises_error(self):
        search_data1 = {
                "year": "2oo4",    
        }
        with self.assertRaises(UserInputError):
            validate_search(search_data1)
        
        search_data2 = {
                "year": "200",    
        }
        with self.assertRaises(UserInputError):
            validate_search(search_data2)


    def test_no_searching_terms_raises_error(self):
        search_data = {}
        with self.assertRaises(UserInputError):
            validate_search(search_data)

    def test_invalid_year_range_input_raises_error(self):
        search_data1 = {
                "year_from": "2024",
                "year_to": "2023",   
        }
        with self.assertRaises(UserInputError):
            validate_search(search_data1)
        
        search_data2 = {
                "year_from": "2024",  
        }
        with self.assertRaises(UserInputError):
            validate_search(search_data2)

