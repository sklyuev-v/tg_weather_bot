# Entry point for bot
from typing import NoReturn
import requests
def input_city(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    answer = 'В городе ' + city + ' ' + str(temperature) + ' °C'




def main() -> NoReturn:
    """
    Entry point for application
    :return: NoReturn
    """
    pass


if __name__ == "__main__":
    main()
