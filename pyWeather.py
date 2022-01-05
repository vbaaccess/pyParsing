from dataclasses import dataclass
import requests
import math

@dataclass
class Weather:
    longitude: float
    latitude: float
    temperature: float
    feels_like: float
    pressure: int
    humidity: int
    clouds: int


def get_weather_for_point(longitude: float, latitude: float) -> Weather:
    """
    Function that collects the weather for a point with a given latitude and longitude.
    1) API (endpoint) used: https://openweathermap.org/api/one-call-api
    2) yourApiKeyFor => To get API_key please register at https://openweathermap.org
    Example of use:
    >>> get_weather_for_point(20, 30)
    Weather(longitude=20, latitude=30, temperature=18.03, feels_like=17.09, pressure=1020, humidity=46, clouds=10)
    """
    API_key = 'yourApiKeyFor'
    data_part = ['current', 'minutely', 'hourly', 'daily', 'alerts']    
    units = ['Standard', 'Metric', 'Imperial']

    args = [latitude, longitude, data_part[3], units[1], API_key]
    url = "https://api.openweathermap.org/data/2.5/onecall"
    url += "?lat={}&lon={}&exclude={}&units={}&appid={}".format(*args)

    r = requests.get(url)
    j = r.json()
    jc = j['current']

    w = Weather(longitude=longitude, latitude=latitude, temperature=round(jc['temp']), feels_like=jc['feels_like'], pressure=jc['pressure'], humidity=jc['humidity'], clouds=jc['clouds'])

    return w
