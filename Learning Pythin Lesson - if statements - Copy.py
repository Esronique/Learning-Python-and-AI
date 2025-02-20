'''
Ask for a city name
Ask the user what temperature it is currently (in Celsius)
If the temperature is greater than 20ºC
Display this sentence:
It is currently warm in Lisbon with a temperature of 20ºC
If the temperature is greater than 10ºC
Display this sentence:
It is currently chilly in Lisbon with a temperature of 15ºC
If the temperature is less than 10ºC
Display this sentence:
It is currently cold in Lisbon with a temperature of 5ºC
If the user didn’t enter a city and temperature
Please try again and enter a city and temperature
'''


temperature = input("What is the current temperature?")
temperature = int(temperature)
rainy = input("Is it raining? (Yes/No) ") 
rainy = rainy.upper()

if temperature >= 20 and rainy == "NO":
    print("Enjoy a sunny day")
elif temperature >= 20 and rainy == "YES":
    print("Don’t forget your umbrella")
elif temperature < 20 and rainy == "NO":
    print("Don’t forget your jacket")
else:
    print("Don’t forget your umbrella and your jacket")


