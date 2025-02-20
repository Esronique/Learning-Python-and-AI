'''
Create a function asking for the city where you are and the current temperature and display this message:
You are in Lisbon and it is currently 17ºC.
Call this function twice.
Bonus point: Display an error message if the user doesn’t enter a city or a temperature
'''


def city_temperature():

  city = input("What city are you in? ")
  temperature = input("What is the temperature in ºC? ")
  if city == "" or temperature == "":
    print("You didn't enter a city or a temperature")
  else:
    print("You are in " + city + " and it is currently " + temperature + "ºC.")


city_temperature()
city_temperature()
