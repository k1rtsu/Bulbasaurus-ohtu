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
            print(value)
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
        author = self.author()
        title = self.title()
        journal = self.journal()
        year = self.year()
        volume = self.volume()

        pages_from = self.pages_from()
        pages_to = self.pages_to()
        line1 = "@article{cite" + year + "\n"
        line2 = "    author = {" + author + "},\n"
        line3 = "    title = {" + title + "},\n"
        line4 = "    journal = {" + journal + "},\n"
        line5 = "    year = {" + year + "},\n"
        line6 = "    volume = {" + volume + "},\n"
        pages_are_specified = pages_from != "" and pages_to != ""
        line7 = ""
        if pages_are_specified:
            line7 = "    pages = {" + pages_from + "--" + pages_to + "}\n"
        line8 = "}"

        return line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8

    def parse_article(self):
        pass

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
