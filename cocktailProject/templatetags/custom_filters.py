from django import template

register = template.Library()

@register.filter
def format_number(value):
    """
    Removes '.0' from whole numbers, otherwise returns the original number.
    """
    try:
        # Check if value is numeric
        if isinstance(value, (int, float)) and value == int(value):
            return int(value)  # Return as integer if it's a whole number
        return value  # Return original value otherwise
    except (ValueError, TypeError):
        return value  # In case of error, return original value