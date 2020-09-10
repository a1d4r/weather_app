import requests
import requests_cache

import secrets

# Cache the weather data for 5 minutes
requests_cache.install_cache('openweather_cache', backend='sqlite', expire_after=600)


class QuotaError(Exception):
    """Exception to be raised when the app exceeds a limit of API calls"""
    pass


def get_weather_data(city):
    """
    Return weather data by a city name.
    Sample data: https://samples.openweathermap.org/data/2.5/weather?q=London&appid=439d4b804bc8187953eb36d2a8c26a02
    """
    url = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(url, params={'q': city, 'appid': secrets.OPEN_WEATHER_API_KEY}).json()

    if response['cod'] == 429:
        # API limit has been reached
        raise QuotaError(response['message'])

    return {
        'city': city,
        'temp': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_weather_data('Kazan'))
