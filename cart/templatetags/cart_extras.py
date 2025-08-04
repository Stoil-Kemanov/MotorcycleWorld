from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.filter
def content_type_id(obj):
    """Get content type ID for an object"""
    return ContentType.objects.get_for_model(obj).id
