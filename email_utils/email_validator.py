import re

def is_valid_email(email):
    """
    Check if the string inside the parameter is a valid email, verified by a specific regex pattern.
    :param email:
    :return Boolean:
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def extract_domain(email):
    """
    Extract the domain(after '@' character) from the string(valid email) from the parameter.
    Raise a `ValueError` if the email is not invalid
    :param email:
    :return String->domain:
    """
    if not is_valid_email(email):
        raise ValueError("Invalid email address")
    return email.split("@")[1]
