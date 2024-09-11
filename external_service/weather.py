from config_data.config import WEATHER_URL_ON_DAY
from config_data.config import WEATHER_URL_ON_5_DAY
import requests
from environs import Env

env = Env()
env.read_env()

OPENWEATHER_API_KEY = env('WEATHER_TOKEN')


def get_weather_on_day(city: str) -> dict:
    params: dict = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url=WEATHER_URL_ON_DAY, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name: str = data['name']
        temp: float = data['main']['temp']
        return f"Погода в {city_name}: {temp}"
    else:
        return "Не удалось получить данные о погоде. Проверьте правильность названия города."


def get_weather_on_5_days(city: str):
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url=WEATHER_URL_ON_5_DAY, params=params)

    if response.status_code == 200:
        data: dict = response.json()
        data_list: list = data['list']
        list_forecast = []

        for el in data_list:
            temp = el['main']['temp']
            date = el['dt_txt']
            print(el)
            list_forecast.append([temp, date])

        return list_forecast
    return None


print(get_weather_on_day('Ярославль'))
print(get_weather_on_5_days('Ярославль'))

# return ('FIVE', DICT)
# return ('DAY', DICT)
