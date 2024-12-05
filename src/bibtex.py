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



class Article(BibTex):
    pass



class Book(BibTex):
    pass



class Inproceedings(BibTex):
    pass



class Misc(BibTex):
    pass

