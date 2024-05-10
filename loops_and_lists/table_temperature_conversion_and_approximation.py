"""
This module converts Fahrenheit temperatures to Celsius using an approximation.

__author__ = "Jackson"
"""

# Initialize variables
fahrenheit = 0

# Print table headers
print("°F    °C    Approx")

# Convert Fahrenheit to Celsius and print the results
while fahrenheit <= 100:
    celsius = (fahrenheit - 30) / 2
    print(f"{fahrenheit}    {celsius:.1f}    {(fahrenheit - 30) / 2:.1f}")
    fahrenheit += 10

if __name__ == "__main__":
    # Test case
    # Input: None
    # Output: Table of Fahrenheit to Celsius conversions
    pass
