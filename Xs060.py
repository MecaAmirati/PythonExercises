n = f = int(input('Qual Número Fatorial deseja descobrir: '))
for c in range(f, 1, -1):
    f *= (c - 1)
print(f'{n}! = {f}')

'''n = int(input('Qual Número Fatorial deseja descobrir: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

'''from math import factorial
n = int(input('Qual Número Fatorial deseja descobrir: '))
f = factorial(n)
print(n)'''
