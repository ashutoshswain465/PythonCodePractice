x = input('Enter the array with spaces between elements: ')
y = [int(item) for item in x.split()]

max_num = max(y)

num_two = 0

for nums in y:
    if num_two < nums < max_num:
        num_two = nums

print(num_two)
