a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = a ^ a
e = c ^ b
f = a & b
g = c | (a ^ a)
e = ~ e

print(f'{d} {e} {f} {g}')
