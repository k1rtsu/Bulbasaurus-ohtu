import re

class UserInputError(Exception):
    pass


def validate_book(author, title, year, publisher):
    if not author or not title or not year or not publisher:
        raise UserInputError("None of the fields can be empty")

    if len(year) != 4:
        raise UserInputError("Year length must be 4")

    if not re.fullmatch("[0-9]+", year):
        raise UserInputError("Year can only consist of numbers")

def validate_article(article_data):
    required_article_data = ['author', 'title', 'year', 'journal', 'volume']
    missing_fields = [
        field for field in required_article_data if not article_data
        .get(field, "")
        .strip()
    ]
    if missing_fields:
        raise UserInputError(f"Missing required fields: {', '.join(missing_fields)}")

    if len(article_data['year']) != 4:
        raise UserInputError("Year length must be 4")

    if not re.fullmatch("[0-9]+", article_data['year']):
        raise UserInputError("Year can only consist of numbers")

    if not re.fullmatch("[0-9]+", article_data['volume']):
        raise UserInputError("Volume can only consist of numbers")

    if article_data['pages_from'] and article_data['pages_to']:
        if article_data['pages_to']<article_data['pages_from']:
            raise UserInputError(
                "The starting page number cannot be greater than the ending page number."
            )

        if not re.fullmatch("[0-9]+", article_data['pages_from']):
            raise UserInputError("Pages can only consist of numbers")

        if not re.fullmatch("[0-9]+", article_data['pages_to']):
            raise UserInputError("Pages can only consist of numbers")

    if article_data['number']:
        if not re.fullmatch("[0-9]+", article_data['number']):
            raise UserInputError("Number can only consist of numbers")
