a = int(input('a: '))
b = int(input('b: '))
operator = int(input('operator: '))

match operator:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case _:
        print('Invalid Input')
