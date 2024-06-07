import string
import random


def generate_random_email(domain="exemple.com"):
    """
    Generate a random Email which contains strings and digits,
    A custom domain can be inserted via the parameter.
    :param domain:
    :return String->randomEmail:
    """
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{local_part}@{domain}"
