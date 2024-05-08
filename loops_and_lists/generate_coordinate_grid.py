# Generate x coordinates using list comprehension
n = 20
a = 1
b = 2
h = (b - a) / n
x = [a + i*h for i in range(n + 1)]
print(x)
