from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o  segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('Analisando...\n')
sleep(1)

'''if n1 > n2 and n1 > n3:
    print('O número {} é o maior!'.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior!'.format(n2))
if n3 > n1 and n3 > n1:
    print('O número {} é o maior!'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor número'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor número'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor número'.format(n1))
if n1 == n2 == n3:
    print('Os números são iguais!')'''

mai = n1
if n2 > n1 and n2 > n3:
    mai = n2
if n3 > n1 and n3 > n2:
    mai = n3
men = n1
if n2 < n1 and n2 < n3:
    men = n2
if n3 < n1 and n3 < n2:
    men = n3
if n1 == n2 == n3:
    print('Os números são iguais!')

print('O maior número é {}.'.format(mai))
print('O menor número é {}.'.format(men))
