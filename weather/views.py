from django.shortcuts import render

from .openweather import get_weather_data
from .models import City


def index(request):
    cities = City.objects.all()
    weather_list = [get_weather_data(city.name) for city in cities]
    context = {'weather_list': weather_list}
    return render(request, 'weather/index.html', context=context)
