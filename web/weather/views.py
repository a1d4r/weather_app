from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect

from .openweather import get_weather_data
from .models import City
from .forms import CityForm


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
    # weather for cities
    cities = City.objects.all()
    cities = [{**get_weather_data(city.name), 'id': city.id} for city in cities]

    # form for adding a city
    form = CityForm()

    context = {'cities': cities, 'form': form}
    return render(request, 'weather/index.html', context=context)


def delete_city(request, city_id):
    City.objects.filter(id=city_id).delete()
    return HttpResponseRedirect(reverse('index'))
