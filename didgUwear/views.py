from datetime import datetime
from didgUwear.models import Shirt, Pant
# from django.http import HttpResponse
from django.shortcuts import render


def closet(request):
    shirt = Shirt.objects.all()
    pant = Pant.objects.all()
    context = {'shirts': shirt, 'pants': pant}
    return render(request, 'didgUwear/closet.jinja', context)


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
