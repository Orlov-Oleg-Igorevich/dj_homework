from audioop import reverse
from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_list_objects = list(Phone.objects.all())
    sr = request.GET.get('sort')
    if sr == 'name':
        phone_list_objects.sort(key=lambda x: x.name)
    elif sr == 'min_price':
        phone_list_objects.sort(key=lambda x: x.price)
    else:
        phone_list_objects.sort(key=lambda x: x.price, reverse=True)
    context = {
        'phones': phone_list_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)



