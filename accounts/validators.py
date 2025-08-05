import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneNumberValidator:
    def __init__(self, message: str = None):
        self.message = message or "Phone number can only contain digits, spaces, hyphens, parentheses, and plus sign."

    def __call__(self, value):
        if not value:  # Allow empty since field is optional
            return

        cleaned = re.sub(r'[\s\-\(\)\+]', '', value)

        if not cleaned.isdigit():
            raise ValidationError(self.message)

        if len(cleaned) < 7 or len(cleaned) > 15:
            raise ValidationError("Phone number must be between 7 and 15 digits.")
