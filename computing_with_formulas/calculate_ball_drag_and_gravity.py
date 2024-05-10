"""
This script calculates the sum of a birth month and date.

__author__ = "Jackson"
"""

# Assigning a birth month and a date
birth_month = 2
birth_date = 6

# Adding the date and month
birth_sum = birth_month + birth_date

# printing the sum
print("Birth Sum:", birth_sum)

if __name__ == "__main__":
    # Test case: Input birth_month = 2, birth_date = 6
    # Expected output: birth_sum = 8
    assert birth_sum == 8, f"Test failed! Expected birth_sum to be 8, but got {birth_sum}"
    print("Test passed!")
