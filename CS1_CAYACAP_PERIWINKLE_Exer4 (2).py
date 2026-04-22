unit = input("Enter the unit of measurement (Celsius, Fahrenheit, Kelvin): ")

if unit != "Celsius" and unit != "Fahrenheit" and unit != "Kelvin":
    print("Invalid")
    exit()

temp = float(input(f"Enter the temperature in {unit}: "))

if unit == "Fahrenheit":
    temp = (temp - 32) * 5 / 9
elif unit == "Kelvin":
    temp = temp - 273.15

if temp < 0:
    print("Too cold!")
elif temp <= 35:
    print("Safe temperature.")
else:
    print("Too hot!")
