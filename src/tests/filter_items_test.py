import unittest
from util import filter_items


class TestFilterItems(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"book_info": {
                "author": "Maija Pythonen",
                "title": "Pythonin alkeet",
                "year": "2009",
                "publisher": "Otava",
                }
            }, 
            {"book_info":{
                "author": "Maik Schmidt",
                "title": "History-based merging of models",
                "year": "2008",
                "publisher": "Otava"
                }
            }
        ]
        self.articles = [{"article_info": {
                "author": "Hanna Javanen",
                "title": "Ketterän ohjelmistotuotannon tulevaisuus",
                "journal": "ATK-lehti",
                "volume": "4",
                "number": "2",
                "year": "2021",
                "pages_from": "89",
                "pages_to": "98",
                "doi": "10.1109/CVSM.2009.5071716",
                "url": "https://sisu.helsinki.fi",
                }
            }
        ]
        self.search_data = {
                "author": "",
                "title": "",
                "year": "",
                "year_from": "",
                "year_to": "",
                "reference_type": "any",
            }

    def test_reference_type_differs_from_search_reference_type(self):
        self.search_data["reference_type"] = "articles"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        self.assertEqual(result, [])
    
    def test_searching_author_without_conditions(self):
        self.search_data["author"] = "Maija"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 1)
    
    def test_searching_author_with_condition_and(self):
        self.search_data["author"] = "Mai AND Schmidt"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 1)

    def test_searching_author_with_condition_or(self):
        self.search_data["author"] = "Mai OR Schmidt"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 2)
    
    def test_searching_title_without_conditions(self):
        self.search_data["title"] = "merging"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 1)
    
    def test_searching_title_with_condition_and(self):
        self.search_data["title"] = "ketterä AND tulevaisuus"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 1)

    def test_searching_title_with_condition_or(self):
        self.search_data["title"] = "ohjelmisto OR python"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 2)

    def test_searching_year(self):
        self.search_data["year"] = "2021"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 1)

    def test_searching_year_range(self):
        self.search_data["year_from"] = "2007"
        self.search_data["year_to"] = "2010"
        result = filter_items(self.books, "books", "book_info", self.search_data)
        result += filter_items(self.articles, "articles", "article_info", self.search_data)
        self.assertEqual(len(result), 2)

    def test_incorrect_search_with_asterisk(self):
        """Test that an asterisk in the beginning of the search does not cause an error
        and returns everything back unchanged.
        """
        self.search_data["author"] = "*Schmidt"
        search_result = filter_items(self.books, "books", "book_info", self.search_data)
        self.assertEqual(self.books, search_result)