import unittest
from util import validate_inproceedings, UserInputError


class TestInproceedingsReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_inproceedings_reference_does_not_raise_error(self):
        validate_inproceedings("Test Author", "Test Title", "2024", "Test Booktitle")

    def test_missing_fields_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Test Author", "Test Title", "2024", None)

    def test_too_short_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Test Author", "Test Title", "202", "Test Booktitle")

    def test_invalid_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Test Author", "Test Title", "year", "Test Booktitle")
