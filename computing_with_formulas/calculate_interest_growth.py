"""
This script calculates the growth amount of an investment after a certain number of years with a given interest rate.

__author__ = "Jackson"
"""

if __name__ == "__main__":
    # Test case
    # Input: p = 1.51, A = 1000, n = 3
    # Expected output: Growth Amount after 3 years: <calculated value>
    p = 1.51  # Interest rate in percent
    A = 1000  # Initial investment amount
    n = 3  # Number of years

    growth_amount = A * (1 + p / 100) ** n

    print("Initial Amount:", A)
    print("Interest Rate:", p, "%")
    print("Growth Amount after", n, "years:", growth_amount)
