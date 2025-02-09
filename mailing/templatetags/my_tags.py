# main/templatetags/my_tags.py

import datetime
from django import template

register = template.Library()


# Создание тега
@register.simple_tag
def limit_text_100(text):
    if len(text) <= 100:
        return text
    else:
        return text[:100]


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.simple_tag
def get_clients(data):
    if data:
        clients = "\n ".join([str(item) for item in data.all()])
        return clients
    return ""
