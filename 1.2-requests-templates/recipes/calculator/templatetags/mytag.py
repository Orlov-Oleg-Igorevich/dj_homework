from django import template
register = template.Library()

@register.simple_tag()
def multiply(qty, unit_price):
    return round(qty * unit_price, 2)