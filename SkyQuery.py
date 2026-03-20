import requests
from datetime import datetime as dt

API_KEY = ""
UNITS = 'standard'
LANG = "eng"
MISSING = "N/A"

class Validate:
    @staticmethod
    def ensure_input(place_holder):
        user_input = input(place_holder).strip().lower()
        if user_input:
            return user_input
        else:
            print(place_holder)

    def validate_city_name(self):
        city_name = Validate.ensure_input("Please enter city name to search: ")
        print("\nSearching...\n")
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}")
        result = response.json()
        if result:
            for index, cities in enumerate (result, start=1):
                print(f"{index}. {cities['name']}, {cities.get('state', MISSING)}, {cities['country']}")
            while True:
                selection = self.ensure_input("Enter your selection: ")
                if not selection.isdigit():
                    print("Please only enter numbers!")
                else:
                    selection = int(selection) - 1
                    return (result[selection]['lat'], result[selection]['lon'])
        else:
            print("Please enter a valid city!")

    @staticmethod
    def utc_to_normal(utc_value):
        converted = dt.fromtimestamp(utc_value)
        time = converted.strftime("%I:%M:%S %p")
        return time

class WeatherData:
    @staticmethod
    def weather_data():
        try:
            validate =  Validate()
            coordinates = validate.validate_city_name()
            URL = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&units={UNITS}&appid={API_KEY}"
            response = requests.get(URL)
            result = response.json()
            if response.status_code != 200:
                print("Weather info for entered location not available!")
                return None
            return result
        except requests.exceptions.RequestException:
            print("Connection timed out, please check your network connection!")
class SkyQuery:
    def __init__(self):
        self.result = WeatherData.weather_data()
        self.weather = self.result['weather'][0]['main']
        self.weather_description = self.result['weather'][0]['description']
        self.temperature = round(float((self.result['main']['temp'])) - 273.17, 3)
        self.temperature_feels_like = round(float(self.result['main']['feels_like']) - 273.17, 3)
        self.humidity = f"{self.result['main']['humidity']}%"
        self.visibility = f"{self.result['visibility']}m"
        self.wind_speed = self.result['wind']['speed']
        self.wind_direction = self.result['wind']['deg']
        self.wind_gust = self.result.get('wind', {}).get('gust', MISSING)
        self.clouds_pct = self.result['clouds']['all']
        self.timezone = f"UTC{(self.result['timezone']//3600):+d}" #:+d tells to always show the sign
        self.sunrise = Validate.utc_to_normal(self.result['sys']['sunrise'])
        self.sunset = Validate.utc_to_normal(self.result['sys']['sunset'])

    def show_data(self):
        try:
            # --- Header Section ---
            print(f"\n--- CURRENT WEATHER: {self.result.get('name', 'Location')} ---")
            print(f"Timezone: {self.timezone} | Condition: {self.weather} ({self.weather_description.title()})")

            # --- Temperature & Feel ---
            print(f"\n🌡️  TEMPERATURE")
            print(f"   Main:        {self.temperature}°C")
            print(f"   Feels Like:  {self.temperature_feels_like}°C")
            print(f"   Clouds:      {self.clouds_pct}% coverage")

            # --- Atmosphere & Wind ---
            print(f"\n💨 ATMOSPHERE")
            print(f"   Wind:        {self.wind_speed} m/s at {self.wind_direction}° (Gusts: {self.wind_gust} m/s)")
            print(f"   Humidity:    {self.humidity}")
            print(f"   Visibility:  {self.visibility}")

            # --- Solar Events ---
            print(f"\n☀️  SOLAR")
            print(f"   Sunrise:     {self.sunrise}")
            print(f"   Sunset:      {self.sunset}")
            print("-" * 35 + "\n")
        except AttributeError:
            pass
