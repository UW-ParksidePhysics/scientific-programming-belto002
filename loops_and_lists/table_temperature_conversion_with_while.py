fahrenheit = 0
print("°F   °C")
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit}   {celsius:.1f}")
    fahrenheit += 10
