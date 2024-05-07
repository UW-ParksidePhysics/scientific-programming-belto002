# define values a and b
a = 3
b = 5

# verify
left = (a+b)**2
right = a**2 + 2*a*b + b**2
print("(a+b)**2 = a**2 + 2*a*b + b**2 is", left == right)

# verify
left = (a-b)**2
right = a**2 - 2*a*b + b**2
print("(a-b)**2 = a**2 - 2*a*b + b**2 is", left == right)
