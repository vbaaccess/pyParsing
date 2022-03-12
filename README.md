### Analyzing and extracting data from content


| Lp  | Example (file)        | Descryption                                       |
|-----|-----------------------|---------------------------------------------------|
| 1   | _pyWeather.py_          | Collect wether data for a earth point                |
| 2   | _pyBinance.py_ | Get candlestick histories for some cryptocurrencies |
| 3   | _pyHotShot.py_    | Tracking promotions in the computer store                               |
| 4   | _pyRecipes.py_           | Collecting some recipes                      |
| 5   | _pyIT_TrendAnalysis.py_    | Tracking technological trends in the IT industry |
| 6   | _pyScrapingRscbFile.py_           | Download of simple data files for further analysis (from rcsb.org) |
| 7   | _pyMovies.py_            | Collect top of movies |
|     |                       |                                                   |


**More details**:

---

1) pyWeather.py
    Function that collects the weather for a point with a given latitude and longitude.
    To use it is required to generate a key for the API of the https://openweathermap.org website.
    After generating the key, substitute it in API_key variable.

    Example of use:
    >>> get_weather_for_point(20, 30)
    Weather(longitude=20, latitude=30, temperature=18.03, feels_like=17.09, pressure=1020, humidity=46, clouds=10)

2) pyBinance.py
    Function that returns candlestick histories for a given symbol and a given interval from a given period of time.
    The data is collected from https://www.binance.com/pl using the API ://api.binance.com/api/v3/klines
    
    Tips:
         1. Documentation: https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data
         2. What is a candle? https://www.kaiko.com/collections/ohlcv
         3. open_time and end_time are given in seconds 
        
3) pyHotShot.py
    Function that takes a hot shot from the selected page and returns all keywords that are contained in the product name.
    Example of use:
    >>> check_hotshot(keywords={'owoce', 'warzywa'})
    (HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100), set())
    >>> check_hotshot(keywords={'nokia'})
    (HotShot(promotion_name='Telefon NoKia 3310', promotion_total_count=100), {'nokia'})
    
4) pyRecipes.py
    Function that downloads links to recipes with a given keyword from the recipe page (www kwestiasmaku com).
    Example of use:
    >>> get_recepie_links("placki")
    {'https://www.kwestiasmaku.com/przepis/placki-kukurydziane',
     'https://www.kwestiasmaku.com/przepis/placki-twarogowe',
     'https://www.kwestiasmaku.com/przepis/placki-z-batatow',
     'https://www.kwestiasmaku.com/przepis/placki-z-ciecierzycy',
     'https://www.kwestiasmaku.com/przepis/placki-z-dyni',
     'https://www.kwestiasmaku.com/przepis/placki-z-kalafiora',
     'https://www.kwestiasmaku.com/przepis/placki-ziemniaczane'}
   
5) pyIT_TrendAnalysis.py
   UNDER CONSTRUCTION - upload pages nfj to bufor

6) pyScrapingRscbFile.py
   Print www content from rcsb.org to analis some data file
   UNDER CONSTRUCTION - parse content and get interesting information
   
7) pyMovies.py
   Print www content from imdb.com top 250 movies
   UNDER CONSTRUCTION - parse content and get interesting information
