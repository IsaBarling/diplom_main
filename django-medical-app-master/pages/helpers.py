from django.core.validators import validate_email
from pydantic import ValidationError


def validate_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False