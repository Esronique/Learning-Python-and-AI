#Ask for a city name
#Display the current weather for this specific city such as
#It is currently 23ºC in Paris, France”

import requests
from rich import print


city = input("What city are you from?")
city= city.strip()

api_key = "3af5d1040392d37b9oa8ta7a106b03d4"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=metric"
api_response = requests.get(api_url)
api_Data = api_response.json()

city = api_Data["city"]
country =api_Data["country"]
temperature = int(api_Data["temperature"]["current"])

print(f"It is currently {temperature}ºC in {city}, {country}")


