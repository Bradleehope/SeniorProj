from datetime import datetime
# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'didgUwear/homepage.htmli')


def closet(request):
    return render(request, 'didgUwear/closet.jinja')


def shirts(request):
    return render(request, 'didgUwear/shirts.jinja')


def pants(request):
    return render(request, 'didgUwear/pants.jinja')


def add(request):
    return render(request, 'didgUwear/add.jinja')


def hello_there(request, name):
    return render(
        request,
        'didgUwear/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
