'''
Create a function that has 3 parameters (a city temperature and humidity level) and display the following message:
The temperature in London is 7 degrees with a humidity of 40%
If the humidity isn’t provided, display the following message:
The temperature in New York is 10 degrees
Call this function twice. one time with humidity and one time without
'''


def city_temperature(city, temperature, humidity=None):
  '''Print city and temperature'''
  if humidity:
    print(
        f"The temperature in {city} is currently {temperature} degrees with a humidity of {humidity}%"
    )
  else:
    print(f"The temperature in {city} is currently {temperature} degrees")


city_temperature("Alberton", 7, 40)
city_temperature("Johannesburg", 20)
