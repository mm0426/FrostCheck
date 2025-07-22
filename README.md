# FrostCheck
Send SMS alerts to your phone when you should bring plants inside due to cold weather

## Overview
FrostCheck monitors tonight's weather forecast using the NOAA Weather API and sends SMS alerts via email-to-SMS gateway when temperatures are expected to drop below your configured threshold.

## How It Works
1. Fetches weather data from the NOAA Weather Service API
2. Checks tonight's forecasted low temperature
3. Compares it against your configured cold threshold
4. Sends SMS alerts via email-to-SMS gateway if it will be too cold

## Setup

### 1. Configure Weather Location
Get your NOAA grid coordinates:
- Visit https://www.weather.gov/ and search your location
- Note the lat/long from the URL you're redirected to
- Enter that in https://api.weather.gov/points/{{lat}},{{long}}
- Copy the office, gridX, and gridY values from the "forecast" URL in the response

### 2. Email Configuration
- Use Gmail or another SMTP email provider
- For Gmail: Enable 2FA and create an app-specific password
- Configure SMTP settings in your .env file

### 3. SMS Gateway Setup
Find your carrier's SMS gateway format:
- **AT&T**: `1234567890@txt.att.net`
- **Verizon**: `1234567890@vtext.com`
- **T-Mobile**: `1234567890@tmomail.net`
- **Sprint**: `1234567890@messaging.sprintpcs.com`

Replace `1234567890` with your actual phone number.

### 4. Environment Variables
Copy `.env.example` to `.env` and configure:
- `office`, `gridx`, `gridy`: Your NOAA grid coordinates
- `coldThreshold`: Temperature threshold (e.g., 32 for freezing)
- `EMAIL_ADDRESS`: Your email address
- `EMAIL_PASSWORD`: Your email app password
- `SMTP_SERVER`: SMTP server (e.g., smtp.gmail.com)
- `SMTP_PORT`: SMTP port (usually 587)
- `SMS_EMAIL`: Your phone's SMS gateway email

## Usage
Run the script manually or set up automated scheduling:
```bash
python frostcheck.py
```

## Scheduling
For automated daily checks, use:
- **Windows**: Task Scheduler
- **macOS/Linux**: cron jobs
- **Cross-platform**: Task Till Dawn (https://www.oliver-matuschin.de/en/projects/task-till-dawn)

## Requirements
- Python 3.x
- Install dependencies: `pip install -r requirements.txt`

## NOAA API Reference
- General info: https://www.weather.gov/documentation/services-web-api
- API docs: https://weather-gov.github.io/api/gridpoints