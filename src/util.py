import re
from urllib.parse import urlparse


class UserInputError(Exception):
    pass


def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


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

    pages_from = article_data.get('pages_from')
    pages_to = article_data.get('pages_to')
    if pages_from and pages_to:
        if pages_to < pages_from:
            raise UserInputError(
                "The starting page number cannot be greater than the ending page number."
            )

        if not re.fullmatch("[0-9]+", pages_from):
            raise UserInputError("Pages can only consist of numbers")

        if not re.fullmatch("[0-9]+", pages_to):
            raise UserInputError("Pages can only consist of numbers")

    number = article_data.get('number')
    if number:
        if not re.fullmatch("[0-9]+", number):
            raise UserInputError("Number can only consist of numbers")

    url = article_data.get('url')
    if url:
        if not is_valid_url(url):
            raise UserInputError("Please enter a valid URL (e.g., 'https://example.com')")


def validate_misc(author, title, year, note):
    if not author or not title or not year:
        raise UserInputError("None of the fields can be empty")

    if len(year) != 4:
        raise UserInputError("Year length must be 4")

    if not re.fullmatch("[0-9]+", year):
        raise UserInputError("Year can only consist of numbers")

    if len(note) > 500:
        raise UserInputError("Note length must be less than 500 words")


def validate_inproceedings(author, title, year, booktitle):
    if not author or not title or not year or not booktitle:
        raise UserInputError("Missing required fields")

    if len(year) != 4:
        raise UserInputError("Year length must be 4")

    if not re.fullmatch("[0-9]+", year):
        raise UserInputError("Year can only consist of numbers")


def validate_edit(edited_info: dict, reference_type: str):
    """Validate the edits made by user."""
    if reference_type == "book":
        validate_book(
            edited_info["author"],
            edited_info["title"],
            edited_info["year"],
            edited_info["publisher"],
        )
    elif reference_type == "article":
        validate_article(edited_info)
    elif reference_type == "misc":
        validate_misc(
            edited_info["author"],
            edited_info["title"],
            edited_info["year"],
            edited_info["note"],
        )
    elif reference_type == "inproceedings":
        validate_inproceedings(
            edited_info["author"],
            edited_info["title"],
            edited_info["year"],
            edited_info["booktitle"],
        )
    else:
        raise ValueError(
            f"The given reference type could not be validated: {reference_type}"
        )
