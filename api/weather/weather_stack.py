import time
import requests
import json
import os

from api.config import WEATHER_STACK_API_KEY, WEATHER_STACK_CITY

FOUR_HOURS_IN_SEC = 4 * 60 * 60
WEATHER_STACK_API_LINK = "http://api.weatherstack.com/forecast?access_key=" + WEATHER_STACK_API_KEY + \
                         "&query=" + WEATHER_STACK_CITY + "&hourly=1"
LOGS_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
OUTPUT_FILE = os.path.join(LOGS_DIRECTORY, "weather_data.json")


def call_weather_stack_api():
    response = requests.get(WEATHER_STACK_API_LINK)
    print(response.json())
    if response.status_code == 200:
        save_weather_data(response.json())
        return True    # Requête réussie
    else:
        return False   # Requête échouée


def save_weather_data(data):
    os.makedirs(LOGS_DIRECTORY, exist_ok=True)
    with open(OUTPUT_FILE, 'w') as file:
        json.dump(data, file)


def run_weather_stack_api_loop():
    while True:
        success = False
        while not success:
            success = call_weather_stack_api()
            if not success:
                time.sleep(60)  # Attendre 1 minute avant de refaire la requête

        time.sleep(FOUR_HOURS_IN_SEC)