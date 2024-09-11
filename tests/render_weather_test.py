import json
from services.render_weather_for_user import render_day_weather

with open('api1.json', 'r') as file:
    WEATHER_DATA = json.loads(file.read())


assert render_day_weather(WEATHER_DATA) == 'Здесь будет красивая визуализация погоды'

# assert fucntion() == result
