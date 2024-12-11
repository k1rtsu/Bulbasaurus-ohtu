import unittest
from util import validate_edit


class TestEditValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_book_edit_does_not_raise_error(self):
        edited_info = {
                "author": "Maija Pythonen",
                "title": "Pythonin alkeet",
                "year": "2009",
                "publisher": "Otava",
                }
        validate_edit(edited_info, "book")

    def test_valid_article_edit_does_not_raise_error(self):
        edited_info = {
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
        validate_edit(edited_info, "article")
        
    def test_valid_misc_edit_does_not_raise_error(self):
        edited_info = {
            "author": "Kaija Sukanen",
            "title": "Olioperustainen ohjelmointi",
            "year": "1986",
            "note": "Laudaturtyö : Helsingin yliopisto, Tietojenkäsittelyopin laitos, 1986."
            }
        validate_edit(edited_info, "misc")
    
    def test_valid_article_edit_does_not_raise_error(self):
        edited_info = {
            "author": "Maik Schmidt",
            "title": "History-based merging of models",
            "year": "2009",
            "booktitle": "2009 ICSE Workshop on Comparison and Versioning of Software Models",
            }
        validate_edit(edited_info, "inproceedings")
        
    def test_edit_raises_error_when_invalid_reference_type(self):
        edited_info = {
            "author": "Maik Schmidt",
            "title": "History-based merging of models",
            "year": "2009",
            "booktitle": "2009 ICSE Workshop on Comparison and Versioning of Software Models",
            }
        with self.assertRaises(ValueError):
            validate_edit(edited_info, "invalid")