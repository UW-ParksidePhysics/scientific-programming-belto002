fahrenheit = 0
print("°F    °C    Approx")
while fahrenheit <= 100:
    celsius = (fahrenheit - 30) / 2
    print(f"{fahrenheit}    {celsius:.1f}    {(fahrenheit - 30) / 2:.1f}")
    fahrenheit += 10
