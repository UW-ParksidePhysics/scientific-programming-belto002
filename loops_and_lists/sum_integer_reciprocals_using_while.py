summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index < maximum_index:
    summation += 1/index
    index += 1

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

# the only thing that needed to be added was increasing index number.
# the maximum index could be fixed to be maximum_index = int(input("Enter a maximum index to be summed: "))
# This will prompt a user to input any number, and it will be typecast to an integer.
