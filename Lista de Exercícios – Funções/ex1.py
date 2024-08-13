def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperatura_fahrenheit = 98.6
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F é equivalente a {temperatura_celsius:.2f}°C")