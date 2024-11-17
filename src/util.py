import re

class UserInputError(Exception):
    pass

def validate_year(year):
    if len(year) != 4:
        raise UserInputError("Year length must be 4")

    
def validate_book(author, title, year, publisher):
    if not author or not title or not year or not publisher:
        raise UserInputError("None of the fields can be empty")

    if len(year) != 4 or not re.fullmatch("[0-9]+", year):
        raise UserInputError("Year length must be 4 and only consist of numbers")
