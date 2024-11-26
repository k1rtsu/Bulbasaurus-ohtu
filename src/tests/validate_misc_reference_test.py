import unittest
from util import validate_misc, UserInputError

class TestMiscReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_misc_reference_does_not_raise_error(self):
        # Testataan, että kelvolliset tiedot eivät aiheuta virhettä
        validate_misc("Test Author", "Test Title", "2001", "This is a valid note.")

    def test_empty_fields_raise_error(self):
        # Testataan, että tyhjät kentät nostavat virheen
        with self.assertRaises(UserInputError):
            validate_misc("", "Test Title", "2001", "Note")
        with self.assertRaises(UserInputError):
            validate_misc("Test Author", "", "2001", "Note")
        with self.assertRaises(UserInputError):
            validate_misc("Test Author", "Test Title", "", "Note")

    def test_invalid_year_raises_error(self):
        # Testataan, että väärän mittainen tai ei-numeerinen vuosi nostaa virheen
        with self.assertRaises(UserInputError):
            validate_misc("Test Author", "Test Title", "20", "Note")
        with self.assertRaises(UserInputError):
            validate_misc("Test Author", "Test Title", "abcd", "Note")

    def test_note_length_exceeds_limit_raises_error(self):
        # Testataan, että liian pitkä note nostaa virheen
        long_note = "a" * 501  # 501 merkkiä pitkä note
        with self.assertRaises(UserInputError):
            validate_misc("Test Author", "Test Title", "2001", long_note)

