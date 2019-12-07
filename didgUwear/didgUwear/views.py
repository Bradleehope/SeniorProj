from didgUwear.models import Shirt, Pant
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import ShirtForm
from django.http import Http404


def closet(request):
    shirt = Shirt.objects.all()
    pant = Pant.objects.all()
    context = {'shirts': shirt, 'pants': pant}
    return render(request, 'didgUwear/closet.jinja', context)


def shirts(request):
    return render(request, 'didgUwear/shirts.jinja')


def pants(request):
    return render(request, 'didgUwear/pants.jinja')


class AddClothes(View):
    def get(self, request):
        form = ShirtForm(request.POST)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ShirtForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                date = datetime.datetime.now()
                s = Shirt(nickname=form['nickname'], primary_color=form['primary_color'],
                          style=form['style'], secondary_color=form['secondary_color'],
                          occasion=form['occasion'], weather=form['weather'],
                          fit=form['pattern'], holiday=form['holiday'], description=form['description'],
                          brand=form['brand'], date_added=date, img_link=form['img_link'])
                print("inserted ")
                s.save()
                return HttpResponse('/closet')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ShirtForm()
        return render(request, 'didgUwear/add.jinja', {'form': form})


class addInputShirt(View):
    def post(self, request):
        form = ShirtForm(request.POST)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ShirtForm(request.POST)
            # check whether it's valid:
            img_link='house.png'
            if form.is_valid():
                date = datetime.datetime.now()
                s = Shirt(nickname=form.cleaned_data['nickname'], primary_color=form.cleaned_data['primary_color'],
                          style=form.cleaned_data['style'], secondary_color=form.cleaned_data['secondary_color'],
                          occasion=form.cleaned_data['occasion'], weather=form.cleaned_data['weather'],
                          holiday=form.cleaned_data['holiday'], description=form.cleaned_data['description'],
                          brand=form.cleaned_data['brand'], date_added=date, img_link=img_link)
                print("inserted ")
                s.save()
                return HttpResponse('/closet')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = ShirtForm()
        return render(request, 'didgUwear/add.jinja', {'form': form})


def style(request):
    return render(request, 'didgUwear/style.jinja')


class StyleInput(View):

    def get(self, request, **kwargs):
        shirtStyle = kwargs['styleinput']
        shirt = Shirt.objects.get(nickname=shirtStyle)
        return JsonResponse(shirt)
