import re

def validate_isbn(isbn):
    return re.match(r"^\d{3}-\d{10}$", isbn)

def validate_date(date):
    return re.match(r"^\d{4}-\d{2}-\d{2}$", date)

def validate_library_id(library_id):
    return re.match(r"^\d{5}$", library_id)
