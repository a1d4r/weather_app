from django.shortcuts import render

from .openweather import get_weather_data


def index(request):
    context = {'weather': get_weather_data('Kazan')}
    return render(request, 'weather/index.html', context=context)
