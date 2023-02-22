import requests

from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):

    api_key = '713d2aecd8ffe2c5a2168f66a4f90082'
    unit = 'Metric'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()  # NOQA
    print(cities)
    all_cities = []

    for city in cities:

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units={unit}&appid={api_key}'
        response = requests.get(url).json()

        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)
