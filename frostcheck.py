
# first, we need to import the necessary libraries

import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
load_dotenv()

# define variables

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMS_EMAIL = os.getenv("SMS_EMAIL")  # recipient's SMS gateway email (e.g., 1234567890@txt.att.net)
weatherAPIUrl = "https://api.weather.gov/gridpoints/" + os.getenv("office") + "/" + os.getenv("gridx") + ","+ os.getenv("gridy") + "/forecast"
coldThreshold = int(os.getenv("coldThreshold"))

# define functions

def getWeatherData():
    response = requests.get(weatherAPIUrl)
    return response.json()

def getTonightsLowTemp(weatherData):
    lowTemp = 999
    for period in weatherData['properties']['periods']:
        if "Tonight" in period['name']:
            lowTemp = period['temperature']
    if lowTemp == 999:
        sendTextMessage("Check the temperature tonight to see if plants need brought in!  There was an error, no low temperature was found for tonight from the NOAA API.")
    return lowTemp

def sendTextMessage(message):
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = SMS_EMAIL
        msg['Subject'] = "FrostCheck Alert"
        
        # Add body to email
        msg.attach(MIMEText(message, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, SMS_EMAIL, text)
        server.quit()
        
        print(f"SMS sent successfully to {SMS_EMAIL}")
        
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# main program

weatherData = getWeatherData()
tonightsLowTemp = getTonightsLowTemp(weatherData)
print(f"Tonight's low temperature is {tonightsLowTemp} degrees.")

if tonightsLowTemp < coldThreshold:
    sendTextMessage("Tonights low is " + str(tonightsLowTemp) + ".  It's going to be too cold tonight! Bring your plants inside!")
else:
    print("It's not going to be too cold tonight.")