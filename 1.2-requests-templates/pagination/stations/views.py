from dataclasses import dataclass

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    count = request.GET.get('page', 1)
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    paginator = Paginator(data, 10)
    page = paginator.get_page(count)


    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
