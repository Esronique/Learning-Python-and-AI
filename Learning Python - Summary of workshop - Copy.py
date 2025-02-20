'''
Ask for the name of the city
Ask the temperature in Celsius
Display the following message
It is currently 15ºC (59ªF) in London.
You should use at least 2 functions, one displaying the message and 1 calculating the Fahrenheit value.
'''


def converte_temperature(temperature_celsius):
    temperature_fahrenheit = 0
    if temperature_celsius:
        temperature_fahrenheit = (int(temperature_celsius) * 9 / 5) + 32

    return temperature_fahrenheit


def display_Message(city, temperature_celsius, temperature_fahrenheit):

    if city and temperature_celsius and temperature_fahrenheit:
        temperature_celsius = int(temperature_celsius)
        temperature_fahrenheit = int(temperature_fahrenheit)
        print(
            f"It is currently {temperature_celsius}ºC ({temperature_fahrenheit}ªF) in {city}."
        )
    else:
        print("Please, enter a valid city and temperature.")


city = input("What city are you in? ")
city = city.capitalize()
temperature = input("What is the current temperature in celcius? ")
temperature = temperature

temperature_fahrenheit = converte_temperature(temperature)
display_Message(city, temperature, temperature_fahrenheit)
