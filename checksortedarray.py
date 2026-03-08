x = input('Enter list elements with space in-between: ')
y = [int(nums) for nums in x.split()]

y_copy_asc = y.copy()
y_copy_desc = y.copy()

y_copy_asc.sort()
y_copy_desc.sort(reverse=True)

if y_copy_asc == y:
    print('Array is sorted in asc order')
elif y_copy_desc == y:
    print('Array is sorted in desc order')
else:
    print('Array not sorted')
