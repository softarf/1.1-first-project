from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    """Печатает текущее время."""
    now_time = datetime.now()
    hour = now_time.strftime('%H')
    minute = now_time.strftime('%M')
    second = now_time.strftime('%S')
    msg = f'Текущее время: {hour}:{minute}:{second}'
    return HttpResponse(msg)


def workdir_view(request):
    """Печатает содержимое текущего каталога (список папок и файлов)."""
    quote = 'Текущий каталог и его содержимое:<br>' + os.getcwd()
    for item in os.listdir():
        quote += '<br>' + ('&nbsp;' * 4) + item
    return HttpResponse(quote)
