"""
This module calculates the summation of the reciprocal of numbers from a starting index to a maximum index.

__author__ = "Jackson"
"""

# Initialize variables
summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

# Calculate summation
while index < maximum_index:
    summation += 1 / index
    index += 1

# Print the result
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

if __name__ == "__main__":
    # Test case
    # Input: starting_index, maximum_index
    # Output: Summation of 1/k from starting_index to maximum_index
    pass

# the only thing that needed to be added was increasing index number.
# the maximum index could be fixed to be maximum_index = int(input("Enter a maximum index to be summed: "))
# This will prompt a user to input any number, and it will be typecast to an integer.
