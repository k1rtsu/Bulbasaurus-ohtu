import unittest
from unittest.mock import Mock
from bibtex import BibTex


class TestBibTex(unittest.TestCase):
    def setUp(self):
        repository_mock = Mock()

        self.reference_uncleaned = {
            "id": "4",
            "type": "inproceedings",
            "author": {"field": "author"},
            "title": {"field": "title"},
            "booktitle": {"field": "booktitle"},
            "journal": {"field": "journal"},
            "volume": {"field": "4"},
            "number": {"field": "2"},
            "year": {"field": "2021"},
            "pages_from": {"field": "89"},
            "pages_to": {"field": "98"},
            "doi": {"field": "doi"},
            "url": {"field": "https://sisu.helsinki.fi"},
            "note": {"field": "note"},
        }
        self.reference_clean = {
            "author": "author",
            "title": "title",
            "booktitle": "booktitle",
            "journal": "journal",
            "volume": "4",
            "number": "2",
            "year": "2021",
            "pages_from": "89",
            "pages_to": "98",
            "doi": "doi",
            "url": "https://sisu.helsinki.fi",
            "note": "note",
        }
        repository_mock.get_reference_info_by_id.return_value = self.reference_uncleaned

        self.bibtex = BibTex(1, repository_mock)

    def test_clean_reference_info_dictionary(self):
        """Test that clean_reference_info_dictionary removes id and type and
        other unwanted data from dictionaries"""
        self.assertEqual(self.bibtex.reference_info, self.reference_clean)
