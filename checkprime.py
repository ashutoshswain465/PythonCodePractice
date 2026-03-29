n = int(input('n: '))

result = True

for i in range(2, int((n ** 0.5) + 1), 1):
    if n == 1:
        result = False
        break
    if n % i == 0:
        result = False
        break

print(result)

