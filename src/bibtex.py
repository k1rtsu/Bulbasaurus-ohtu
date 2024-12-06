from get_references import get_reference_info_by_id


def create_reference_object(reference_id):
    """Create an object from the reference"""
    reference_info = get_reference_info_by_id(reference_id)
    reference_type = reference_info["type"]

    if reference_type == "article":
        return Article(reference_info)
    if reference_type == "book":
        return Book(reference_info)
    if reference_type == "inproceedings":
        return Inproceedings(reference_info)
    if reference_type == "misc":
        return Misc(reference_info)

    raise ValueError(f"Wrong reference_type: {reference_type}")


class BibTex:
    """Super class for Article, Book, Inproceedings and Misc"""
    def __init__(self, reference_info: dict):
        self.reference_info = reference_info
        self.reference_type = reference_info["type"]
        self.reference_id = reference_info["id"]
        self.clean_reference_info_dictionary()

    def clean_reference_info_dictionary(self):
        """Make reference_info dictionary simpler by extractig only the values we need
        for the BibTex references"""
        new_dictionary = {}
        for value in self.reference_info:
            if value not in ("id", "type"):
                new_dictionary[value] = self.reference_info[value]["field"]

        self.reference_info = new_dictionary

    def type(self):
        return self.reference_type

    def author(self):
        return self.reference_info["author"]

    def title(self):
        return self.reference_info["title"]

    def year(self):
        return self.reference_info["year"]


class Article(BibTex):

    def write_bibtex_reference(self) -> str:
        first_line = "@article{citekey\n"
        required_info = self.required_info()
        pages = self.pages()
        last_line = "}"

        return first_line + required_info + pages + last_line

    def required_info(self):
        text = ""
        required_info = ["author", "title", "year", "journal", "volume"]
        for key, value in self.reference_info.items():
            if key in required_info:
                text += "    " + key + "= {" + value + "},\n"
        return text

    def pages(self):
        pages_from = self.pages_from()
        pages_to = self.pages_to()

        text = ""
        pages_are_specified = pages_from != "" and pages_to != ""
        if pages_are_specified:
            text = "    pages = {" + pages_from + "--" + pages_to + "}\n"

        return text

    def journal(self):
        return self.reference_info["journal"]

    def volume(self):
        return self.reference_info["volume"]

    def pages_from(self):
        return self.reference_info["pages_from"]

    def pages_to(self):
        return self.reference_info["pages_to"]


class Book(BibTex):
    def write_bibtex_reference(self) -> str:
        author = self.author()
        title = self.title()
        year = self.year()
        publisher = self.publisher()
        return [author, title, year, publisher]

    def publisher(self):
        return self.reference_info["publisher"]


class Inproceedings(BibTex):
    def write_bibtex_reference(self) -> str:
        author = self.author()
        title = self.title()
        year = self.year()
        booktitle = self.booktitle()
        return [author, title, year, booktitle]

    def booktitle(self):
        return self.reference_info["booktitle"]


class Misc(BibTex):
    def write_bibtex_reference(self) -> str:
        return
