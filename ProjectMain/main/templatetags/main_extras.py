from django import template

register = template.Library()


@register.filter
def class_title(value):
    """Converts a class slug like 'reptiles' to 'Reptiles'."""
    return value.replace('-', ' ').title()
