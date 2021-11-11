c = 0
n = 0
for x in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        c += n
print('A soma dos valores pares é {}.'.format(c))
