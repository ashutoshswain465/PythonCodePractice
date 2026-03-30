a = int(input('a: '))
b = int(input('b: '))

num = a if a > b else b

while not (num % a == 0 and num % b == 0):
    num += 1

print(num)
