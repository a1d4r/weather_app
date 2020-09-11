from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .openweather import get_weather_data
from .models import City
from .forms import CityForm


def index(request):
    # weather for cities
    cities = City.objects.all()
    weather_list = [get_weather_data(city.name) for city in cities]

    # form for adding a city
    form = CityForm()

    context = {'weather_list': weather_list, 'form': form}
    return render(request, 'weather/index.html', context=context)


def new_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
