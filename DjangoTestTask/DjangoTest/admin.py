from django.contrib import admin
from DjangoTest.models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'url', 'named_url')
    list_filter = ('menu_name',)
