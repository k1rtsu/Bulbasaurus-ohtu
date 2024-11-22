import unittest
from util import validate_article, UserInputError


class TestArticleReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_book_reference_does_not_raise_error(self):
        article_data = {
                "author": "TestAuthor",
                "title": "TestTitle",
                "journal": "TestJournal",
                "volume": "33",
                "number": "2",
                "year": "2024",
                "pages_from": "22",
                "pages_to": "23",
                "doi": "TestDoi",
                "url": "https://www.example.com"
        }
        validate_article(article_data)


    def test_invalid_year_raises_error(self):
        article_data = {
                "author": "TestAuthor",
                "title": "TestTitle",
                "journal": "TestJournal",
                "volume": "33",
                "year": "2oo4",
                
        }
        with self.assertRaises(UserInputError):
            validate_article(article_data)


    def test_missing_fields_raises_error(self):
        article_data = {
                "title": "TestTitle",
                "journal": "TestJournal",
                "volume": "33",
                "year": "2oo4",
                
        }
        with self.assertRaises(UserInputError):
            validate_article(article_data)

    def test_invalid_pages_input_raises_error(self):
        article_data = {
                "author": "TestAuthor",
                "title": "TestTitle",
                "journal": "TestJournal",
                "volume": "33",
                "year": "2oo4",
                "pages_from": "23",
                "pages_to": "22",
                
        }
        with self.assertRaises(UserInputError):
            validate_article(article_data)
    
    def test_invalid_url_input_raises_error(self):
        article_data = {
                "author": "TestAuthor",
                "title": "TestTitle",
                "journal": "TestJournal",
                "volume": "33",
                "year": "2oo4",
                "url": "ww.test.fi",         
        }
        with self.assertRaises(UserInputError):
            validate_article(article_data)
