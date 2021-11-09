from time import sleep
n = int(input('Digite um número: '))
print('Analisando...')
r = n % 2 # % usa o resto da divisão
sleep(2)
if r == 1:
    print('{} é um número ímpar.'.format(n))
else:
    print('{} é um número par.'.format(n))
