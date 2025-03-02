# FrostCheck
Send message to my phone if I should bring plants in tonight

Messages are sent to my phone via a telegram bot which was setup using the steps outlined here - https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python

I'm handing task scheduling using task till dawn located here - https://www.oliver-matuschin.de/en/projects/task-till-dawn

Some info about the noaa.gov api is here - https://www.weather.gov/documentation/services-web-api, https://weather-gov.github.io/api/gridpoints.  I ultimately searched my zip code from their main page, noted the lat/log part of the url that I was redirected to, entered that in https://api.weather.gov/points/{{lat}},{{log}}, and copied the office, gridx, and gridy parts from the url under "forecast" in the response body.