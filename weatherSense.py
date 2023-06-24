#https://openweathermap.org/api
import argparse
import pyfiglet
from simple_chalk import chalk
import requests

#API key for openweathermap
API_KEY = "887aa8f495cc06a76573fa9bc8670b36"

#BASE URL for openweathermap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Map the weather codes to the weather icons
WEATHER_MAP = {

    #day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "🌩",
    "13d": "🌨",
    "50d": "🌫",

    #night icons
    "01n": "🌙",
    "02n": "🌙⛅️",
    "03n": "🌙☁️",
    "04n": "🌙☁️",
    "09n": "🌙🌧",
    "10n": "🌙🌦",
    "11n": "🌙🌩",
    "13n": "🌙🌨",
    "50n": "🌙🌫",

}

# Construct API URL with query parameters
parser = argparse.ArgumentParser(description="Check weather for a certain country/city")
parser.add_argument("country", help="The country/city you want to check the weather for")
args = parser.parse_args()
query_params = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make API request and parse response using requests library
response = requests.get(query_params)
if response.status_code != 200:
    print(chalk.red("Error: Unable to fetch weather data"))
    exit()

# Parse the JSON response from API and extract relevant data
weather_data = response.json()

#Get information from response
temp=weather_data["main"]["temp"]
feels_like = weather_data["main"]["feels_like"]
description = weather_data["weather"][0]["description"]
icon = weather_data["weather"][0]["icon"]
city = weather_data["name"]
country = weather_data["sys"]["country"]

#construct the output with weather icon
icon=WEATHER_MAP.get(icon, "")
result = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
result += f"{icon}, {description} \n"
result += f"Temperature: {temp}°C \n"
result += f"Feel like: {feels_like}°C \n"

#Print the output
print(chalk.green(result))





