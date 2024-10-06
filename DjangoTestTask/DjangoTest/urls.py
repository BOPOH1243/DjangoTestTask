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
    path('combined-menus/', views.combined_menus, name='combined_menus'),
    path('drinks/', views.drinks, name='drinks'),
    path('alcoholic-drinks/', views.alcoholic_drinks, name='alcoholic_drinks'),
    path('non-alcoholic-drinks/', views.non_alcoholic_drinks, name='non_alcoholic_drinks'),
    path('rum/', views.rum, name='rum'),
    path('vodka/', views.vodka, name='vodka'),
    path('juice/', views.juice, name='juice'),
    path('tea/', views.tea, name='tea'),
]
