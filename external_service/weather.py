from config_data.config import WEATHER_URL_ON_DAY
from config_data.config import WEATHER_URL_ON_5_DAY
from config_data.config import OPENWEATHER_API_KEY
import requests


def get_weather_on_day(city: str) -> str:
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
            city_name = el['city']['name']
            list_forecast.append([temp, date, city_name])

        return list_forecast
    return None