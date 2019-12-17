from didgUwear.models import Shirt, Pant
import datetime
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import ShirtForm, PantForm, FilterForm


def closet(request):
    shirt = Shirt.objects.all()
    pant = Pant.objects.all()
    form = FilterForm
    context = {'shirts': shirt, 'pants': pant, 'form': form}
    return render(request, 'didgUwear/closet.jinja', context)


def shirts(request):
    shirt = Shirt.objects.all()
    context = {'shirts': shirt}
    return render(request, 'didgUwear/shirts.jinja', context)


def pants(request):
    pant = Pant.objects.all()
    context = {'pants': pant}
    return render(request, 'didgUwear/pants.jinja', context)


class AddPant(View):
    def get(self, request):
        form = PantForm()
        return render(request, 'didgUwear/addPant.jinja', {'form': form})


class addInputPant(View):
    def post(self, request):
        form = PantForm(request.POST, request.FILES)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PantForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                date = datetime.datetime.now()
                p = Pant(nickname=form.cleaned_data['nickname'], primary_color=form.cleaned_data['primary_color'],
                         style=form.cleaned_data['style'], description=form.cleaned_data['description'],
                         brand=form.cleaned_data['brand'], date_added=date, img_link=form.cleaned_data['img_link'])
                print("inserted ")
                p.save()
                return render(request, 'didgUwear/closet.jinja')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = PantForm()
        return render(request, 'didgUwear/addPant.jinja', {'form': form})


class AddShirt(View):
    def get(self, request):
        form = ShirtForm()
        return render(request, 'didgUwear/addShirt.jinja', {'form': form})


class addInputShirt(View):
    def post(self, request):
        form = ShirtForm(request.POST, request.FILES)
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ShirtForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                date = datetime.datetime.now()
                s = Shirt(nickname=form.cleaned_data['nickname'], primary_color=form.cleaned_data['primary_color'],
                          style=form.cleaned_data['style'], secondary_color=form.cleaned_data['secondary_color'],
                          occasion=form.cleaned_data['occasion'], weather=form.cleaned_data['weather'],
                          holiday=form.cleaned_data['holiday'], description=form.cleaned_data['description'],
                          brand=form.cleaned_data['brand'], date_added=date, img_link=form.cleaned_data['img_link'])
                print("inserted ")
                s.save()
                return render(request, 'didgUwear/closet.jinja')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = ShirtForm()
            return render(request, 'didgUwear/addShirt.jinja', {'form': form})


class DeleteItem(View):
    def get(self, request, **kwargs):
        if kwargs['clothing'] == 'pants':
            Pant.objects.filter(nickname=kwargs['nickname']).delete()
        else:
            Shirt.objects.filter(nickname=kwargs['nickname']).delete()
        print("deleting")
        return render(request, 'didgUwear/closet.jinja')


def style(request):
    return render(request, 'didgUwear/style.jinja')


class StyleInput(View):

    def get(self, request, **kwargs):
        shirtStyle = kwargs['styleinput']
        shirt = Shirt.objects.get(nickname=shirtStyle)
        return JsonResponse(shirt)
