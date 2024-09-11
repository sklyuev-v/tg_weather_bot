import os
from environs import Env


# Путь к папке с токенами
TOKENS_DIR: str = os.path.join(os.path.dirname(__file__), 'tokens')

# Чтение токенов из файлов
def read_token(file_name: str) -> str:
    with open(os.path.join(TOKENS_DIR, file_name), 'r') as file:
        return file.read().strip()

# # Ключи для Telegram и OpenWeatherMap
# TELEGRAM_API_TOKEN: str = read_token('telegram_token.txt')
# OPENWEATHER_API_KEY: str = read_token('openweather_token.txt')

# URL для обращения к API погоды
WEATHER_URL_ON_DAY: str = "https://api.openweathermap.org/data/2.5/weather" # https://openweathermap.org/current#name (https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key})
WEATHER_URL_ON_5_DAY: str = "https://api.openweathermap.org/data/2.5/forecast" # (api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}) api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}


env: Env = Env()
env.read_env()
print(env('BOT_TOKEN'))
print(env('WEATHER_TOKEN'))
