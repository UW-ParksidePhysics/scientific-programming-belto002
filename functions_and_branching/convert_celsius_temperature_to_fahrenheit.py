def convert_celsius_to_fahrenheit(celsius_temperature):
  """convert temperature from celsius to fahrenheit"""
  return (9./5.)*celsius_temperature + 32


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
  """convert temperature from fahrenheit to celsius"""
  return (5./9.)*(fahrenheit_temperature - 32)


if __name__ == "__main__":
  celsius_temperatures = [0, 21, 100]
  print('T_C\tT_C(T_F(T_C))')
  
  for some_celsius_temperature in celsius_temperatures:
    converted_temperature = convert_fahrenheit_to_celsius(convert_celsius_to_fahrenheit
  (some_celsius_temperature))
    print(f'{some_celsius_temperature}\t\t{converted_temperature:.0f}') 



  