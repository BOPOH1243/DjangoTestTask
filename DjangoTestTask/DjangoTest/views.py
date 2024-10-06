# DjangoTest/views.py
from django.shortcuts import render
from django.db import connection

def animals(request):
    # Логика формирования контекста для страницы
    context = {}

    # Возврат отрендеренного шаблона
    response = render(request, 'animals.html', context)

    # Вывод количества запросов к БД
    print(f"Количество запросов к БД: {len(connection.queries)}")

    return response

def combined_menus(request):
    return render(request, 'combined_menus.html')

def feline(request):
    return render(request, 'feline.html')

def canine(request):
    return render(request, 'canine.html')

def cat(request):
    return render(request, 'cat.html')

def cheetah(request):
    return render(request, 'cheetah.html')

def fox(request):
    return render(request, 'fox.html')

def dog(request):
    return render(request, 'dog.html')

# Вьюхи для меню с напитками
def drinks(request):
    return render(request, 'drinks.html')

def alcoholic_drinks(request):
    return render(request, 'alcoholic_drinks.html')

def non_alcoholic_drinks(request):
    return render(request, 'non_alcoholic_drinks.html')

def rum(request):
    return render(request, 'rum.html')

def vodka(request):
    return render(request, 'vodka.html')

def juice(request):
    return render(request, 'juice.html')

def tea(request):
    return render(request, 'tea.html')
