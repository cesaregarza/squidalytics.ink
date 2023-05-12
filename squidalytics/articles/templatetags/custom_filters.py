from django import template

register = template.Library()


@register.filter
def replace(value: str, args: str) -> str:
    search_str, replacement_str = args.split(",")
    return value.replace(search_str, replacement_str)
