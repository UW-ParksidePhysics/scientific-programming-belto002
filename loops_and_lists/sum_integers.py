"""
This module calculates the summation of integers from 1 to a maximum integer and compares it with the formula result.

__author__ = "Jackson"
"""

# Initialize variables
maximum_integer = 100
sum_result = 0

# Calculate summation using loop
for i in range(1, maximum_integer + 1):
    sum_result += i

# Calculate result using formula
formula_result = maximum_integer * (maximum_integer + 1) / 2

# Print results
print(f"n = {maximum_integer}")
print(f"sum(1, n) = {sum_result}")
print(f"n(n+1)/2 = {formula_result}")

if __name__ == "__main__":
    # Test case
    # Input: maximum_integer
    # Output: sum_result, formula_result
    pass
