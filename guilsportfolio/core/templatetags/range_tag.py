from django import template
register = template.Library()


@register.filter(name='num_range')
def range_tag_function(number):
    return range(number)

