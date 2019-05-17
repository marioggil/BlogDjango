from django import template
import random
register = template.Library()

@register.simple_tag

def random_int(b):
    n = random.randint(2,b)
    return n
