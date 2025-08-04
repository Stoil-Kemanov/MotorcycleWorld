from django import template
from accounts.utils import get_compatibility_color

register = template.Library()

@register.filter
def compatibility_color(score):
    """Get Bootstrap color class for compatibility score"""
    try:
        return get_compatibility_color(float(score))
    except (ValueError, TypeError):
        return "secondary"  # Default color if score is invalid
