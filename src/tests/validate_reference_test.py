import unittest
from util import validate_book, UserInputError


class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_book_reference_does_not_raise_error(self):
        validate_book("Test Author", "Test Title", "2001", "Test Publisher")


    def test_too_short_or_unproper_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_book("Test Author", "Test Title", "200", "Test Publisher")

        with self.assertRaises(UserInputError):
            validate_book("Test Author", "Test Title", "2oo1", "Test Publisher")

    def test_missing_fields_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_book("Test Author", "Test Title", "2001")
