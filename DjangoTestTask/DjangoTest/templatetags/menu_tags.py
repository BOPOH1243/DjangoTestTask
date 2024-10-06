# DjangoTest/templatetags/menu_tags.py
from django import template
from DjangoTest.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {
        'menu_items': menu_items,
        'current_url': current_url
    }
