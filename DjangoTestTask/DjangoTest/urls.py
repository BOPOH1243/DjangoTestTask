# DjangoTest/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.animals, name='animals'),
    path('feline/', views.feline, name='feline'),
    path('canine/', views.canine, name='canine'),
    path('cat/', views.cat, name='cat'),
    path('cheetah/', views.cheetah, name='cheetah'),
    path('fox/', views.fox, name='fox'),
    path('dog/', views.dog, name='dog'),
]
