# DjangoTest/views.py
from django.shortcuts import render

def animals(request):
    return render(request, 'animals.html')

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
