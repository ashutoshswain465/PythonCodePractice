n = int(input('n: '))

for i in range(n):
    if i == 0:
        print('* ')
    elif i == (n - 1):
        print('* ' * n)
    else:
        print('* ' + '  '*(i - 1) + '* ')
