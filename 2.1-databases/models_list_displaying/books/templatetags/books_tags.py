from django import template

register = template.Library()

@register.simple_tag()
def get_date(page):
    return page.object_list[0].pub_date