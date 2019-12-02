from didgUwear.models import Shirt, Pant
from datetime import datetime
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

    def post(self, request):
        form = ShirtForm(request.POST)
        if form.is_valid():
            form.cleaned_data()
            print("form ", form)
            date = datetime.today().strftime('%Y-%m-%d')
            s = Shirt(nickname=form['nickname'], primary_color=form['primary_color'],
                      style=form['style'], secondary_color=form['secondary_color'],
                      occasion=form['occasion'], weather=form['weather'],
                      pattern=form['pattern'], holiday=form['holiday'], description=form['description'],
                      brand=form['brand'], date_added=date, img_link=form['img_link'])
            print("form ")
            s.save()
            return HttpResponse('/closet')
        else:
            print("no")
            raise Http404


class addInputShirt(View):
    def get(self, request, **kwargs):
        date = datetime.datetime.now()
        s = Shirt(nickname=kwargs['nickname'], primary_color=kwargs['primary_color'],
                  style=kwargs['style'], secondary_color=kwargs['secondary_color'],
                  occasion=kwargs['occasion'], weather=kwargs['weather'],
                  fit=kwargs['fit'], holiday=kwargs['holiday'], description=kwargs['description'],
                  brand=kwargs['brand'], date_added=date, img_link=kwargs['img_link'])
        s.save()
        return JsonResponse()


def style(request):
    return render(request, 'didgUwear/style.jinja')


class StyleInput(View):

    def get(self, request, **kwargs):
        shirtStyle = kwargs['styleinput']
        shirt = Shirt.objects.get(nickname=shirtStyle)
        return JsonResponse(shirt)
