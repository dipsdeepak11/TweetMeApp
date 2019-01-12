from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if value == '':
        raise ValidationError('its cannot be empty')
    return value
