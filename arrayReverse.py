x = input('Enter the array with spaces between elements: ')
y = [int(item) for item in x.split()]
result = y[::-1]
print(result)
