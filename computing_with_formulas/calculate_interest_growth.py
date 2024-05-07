# US government securities nominal 3-year rate as of 2021-09-15 is 1.51%
p = 1.51

A = 1000
n = 3

growth_amount = A * (1 + p / 100)**n

print("Initial Amount:", A)
print("Interest Rate:", p, "%")
print("Growth Amount after", n, "years:", growth_amount)
