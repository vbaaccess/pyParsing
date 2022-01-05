# pyParsing
Analyzing and extracting data from content

1) pyWeather.py
    Function that collects the weather for a point with a given latitude and longitude.
    To use it is required to generate a key for the API of the https://openweathermap.org website.
    After generating the key, substitute it in API_key variable.

    Example of use:
    >>> get_weather_for_point(20, 30)
    Weather(longitude=20, latitude=30, temperature=18.03, feels_like=17.09, pressure=1020, humidity=46, clouds=10)
