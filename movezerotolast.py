x = input('Enter list items with a space in-between: ')
y = [int(nums) for nums in x.split()]

for num in y:
    if num == 0:
        i = y.index(0)
        y.pop(i)
        y.append(0)

print(y)
