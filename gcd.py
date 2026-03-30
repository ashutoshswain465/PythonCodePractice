a = int(input('a: '))
b = int(input('b: '))

num = a if a < b else b

while not (a % num == 0 and b % num == 0):
    num -= 1

print(num)
