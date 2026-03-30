def checkprime(num):
    result = True
    for i in range(2, int((num ** 0.5) + 1), 1):
        if num == 1:
            result = False
            break
        if num % i == 0:
            result = False
            break

    return result


n = int(input('n: '))

isPrime = False
n += 1

while not isPrime:
    isPrime = checkprime(n)
    if isPrime:
        print(n)
    else:
        n += 1
