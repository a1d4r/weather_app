from django import forms
from django.core.exceptions import ValidationError

from .models import City
from .openweather import get_weather_data, NoSuchCityError


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    def clean_name(self):
        city_name = self.cleaned_data['name']

        try:
            weather_data = get_weather_data(city_name)
        except NoSuchCityError as e:
            raise ValidationError(f'City not found: {city_name}')

        return city_name
