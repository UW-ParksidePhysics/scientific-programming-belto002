maximum_integer = 100

sum_result = 0
for i in range(1, maximum_integer+1):
    sum_result += i

formula_result = maximum_integer * (maximum_integer + 1) / 2

print(f"n = {maximum_integer}")
print(f"sum(1, n) = {sum_result}")
print(f"n(n+1)/2 = {formula_result}")
