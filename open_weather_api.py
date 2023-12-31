import requests
import logging
import os

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def main():

    key = os.environ.get('WATHER_KEY')
    
    if key is None:
        logging.warning('Environment Variable "WEATHER_KEY" not found')
        return
    
    city_country = input('What location would you like a 5-day forecast for: ').lower()

    if city_country is None:
        print('Error - Please enter a city in the following format "city,country code"')
        return

    query = {'q': city_country, 'units': 'imperial', 'appid': key}


    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    city_name = data['city']['name']

    forecast_items = data['list']

    for forecast in forecast_items:
        date = forecast['dt_txt']   # Using city timezone as why would someone in X city want to know what time it is in UTC.
        temp = forecast['main']['temp']
        wind_speed = forecast['wind']['speed']
        weather = forecast['weather'][0]['description']
        print(f'at {date} local time, it will be {weather} with a temperature of {temp}F in {city_name}, The wind speed is {wind_speed} miles per hour.')
        logging.debug(f'DATE: {date}, CITY: {city_name}')

if __name__ == '__main__':
    logging.info('5 Day Forecast Program Launched')
    main()


'''
Part 2
Doesn't make sense to use UNIX time when the local time is not only more relevant to the forecast
but it's available in the JSON

Part 3
logs should be used when the information should only be viewed by developers
Prints are to be viewed by users and should be printed in a user-friendly manor
You should NEVER log sensitive information such as keys,
as while logs are made to be viewed by developers, they can still be accessed by users.
'''