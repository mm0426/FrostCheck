
# first, we need to import the necessary libraries

import requests
import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
load_dotenv()

# define variables

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
weatherAPIUrl = "https://api.weather.gov/gridpoints/" + os.getenv("office") + "/" + os.getenv("gridx") + ","+ os.getenv("gridy") + "/forecast"
coldThreshold = int(os.getenv("coldThreshold"))

# define functions

def getWeatherData():
    response = requests.get(weatherAPIUrl)
    return response.json()

def getTonightsLowTemp(weatherData):
    lowTemp = 70
    for period in weatherData['properties']['periods']:
        if "Tonight" in period['name']:
            lowTemp = period['temperature']
    return lowTemp

def sendTextMessage(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    print(requests.get(url).json())

# main program

weatherData = getWeatherData()
tonightsLowTemp = getTonightsLowTemp(weatherData)
print(f"Tonight's low temperature is {tonightsLowTemp} degrees.")

if tonightsLowTemp < coldThreshold:
    sendTextMessage("Tonights low is " + str(tonightsLowTemp) + ".  It's going to be too cold tonight! Bring your plants inside!")
else:
    print("It's not going to be too cold tonight.")