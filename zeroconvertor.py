def neg(n):
    for i in range(n, 1):
        print(i, end=' ')


def pos(n):
    for i in range(n - 1, -1, -1):
        print(i, end=' ')


num = int(input("n: "))

if num == 0:
    print('already zero')
elif num < 0:
    neg(num)
else:
    pos(num)
