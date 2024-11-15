class UserInputError(Exception):
    pass

def validate_year(year):
    if len(year) != 4:
        raise UserInputError("Year length must be 4")

    
