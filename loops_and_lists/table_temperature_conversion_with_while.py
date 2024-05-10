"""
This module converts Fahrenheit temperatures to Celsius.

__author__ = "Jackson"
"""

# Initialize variables
fahrenheit = 0

# Print table headers
print("°F   °C")

# Convert Fahrenheit to Celsius and print the results
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit}   {celsius:.1f}")
    fahrenheit += 10

if __name__ == "__main__":
    # Test case
    # Input: None
    # Output: Table of Fahrenheit to Celsius conversions
    pass
