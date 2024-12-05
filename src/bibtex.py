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
    pass



class Book(BibTex):
    pass



class Inproceedings(BibTex):
    pass



class Misc(BibTex):
    pass

