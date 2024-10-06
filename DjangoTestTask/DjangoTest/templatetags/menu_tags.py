from django import template
from DjangoTest.models import MenuItem

register = template.Library()

def get_active_menu(menu_items, current_url):
    """ Рекурсивная функция для нахождения активного пункта меню и всех его родителей """
    for item in menu_items:
        if item.get_absolute_url() == current_url:
            return [item]
        children = get_active_menu(item.children.all(), current_url)
        if children:
            return [item] + children
    return []

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    
    # Теперь мы фильтруем по имени меню
    menu_items = MenuItem.objects.filter(parent__isnull=True, menu_name=menu_name).prefetch_related('children')

    active_items = get_active_menu(menu_items, current_url)
    
    return {
        'menu_items': menu_items,
        'active_items': active_items,
        'current_url': current_url
    }
