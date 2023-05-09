from _decimal import *

user_temperature_celsius = float(input('Enter the temperature in Celsius >>> '))
if type(user_temperature_celsius) == float:
    user_temperature_fahrenheit = (user_temperature_celsius * 1.8) + 32
    result_fahrenheit = Decimal(str(user_temperature_fahrenheit)).quantize(Decimal('0.1'))
    print(result_fahrenheit)
