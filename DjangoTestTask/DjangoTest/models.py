# DjangoTest/models.py
from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url or '#'

    def __str__(self):
        return self.name
