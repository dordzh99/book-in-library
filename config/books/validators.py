from datetime import date

from django.core.exceptions import ValidationError

def validate_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(
            f'Укажите год не больше {current_year}'
        )
    return value
