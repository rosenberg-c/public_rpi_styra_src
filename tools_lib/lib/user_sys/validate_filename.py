import re


def _transform_filename(string):
    string = str(string).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', string)


def get_valid_filename(string):
    name = _transform_filename(string)
    if string == name and string != "":
        return True
    return False
