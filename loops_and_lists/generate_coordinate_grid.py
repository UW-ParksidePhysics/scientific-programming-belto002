"""
This module generates x coordinates using list comprehension.

__author__ = "Jackson"
"""

# Generate x coordinates using list comprehension
n = 20
a = 1
b = 2
h = (b - a) / n
x = [a + i * h for i in range(n + 1)]
print(x)

if __name__ == "__main__":
    # Test case
    # Input: n (number of intervals), a (start), b (end)
    # Output: List of x coordinates
    pass
