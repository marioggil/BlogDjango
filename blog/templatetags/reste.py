from django import template

register = template.Library()

@register.simple_tag
def reste(value):
    return value-1
