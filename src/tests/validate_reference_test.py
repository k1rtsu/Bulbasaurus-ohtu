import unittest
from util import validate_year, UserInputError


class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_year_length_does_not_raise_error(self):
        validate_year("2001")



