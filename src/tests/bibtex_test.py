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

    def test_reference_in_bibtex_form(self):
        """Reference is returned in the correct bibtex form"""
        bibtex_form = self.bibtex.reference_in_bibtex_form()
        correct_form = self.correct_bibtex_form()
        self.assertEqual(bibtex_form, correct_form)

    def correct_bibtex_form(self):
        text = ""
        text += '@inproceedings{citekey,\n'
        text += '    author = {author},\n'
        text += '    title = "{title}",\n'
        text += '    booktitle = "{booktitle}",\n'
        text += '    journal = "{journal}",\n'
        text += '    volume = "{4}",\n'
        text += '    number = "{2}",\n'
        text += '    year = "{2021}",\n'
        text += '    pages = {89--98},\n'
        text += '    doi = "{doi}",\n'
        text += '    url = "{https://sisu.helsinki.fi}",\n'
        text += '    note = "{note}",\n'
        text += '}'
        return text
