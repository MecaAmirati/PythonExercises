n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('{} é maior que é {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que é {}'.format(n2, n1))
else:
    print('Os valores são iguais.')
