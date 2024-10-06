from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    
    # Добавляем поле для названия меню
    menu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.url if self.url else reverse(self.named_url)
