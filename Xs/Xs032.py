from time import sleep
from datetime import date
n = int(input('Digite qual ano quer analisar ou digite "0" para analisar o ano atual: '))
if n == 0:
    n = date.today().year
print('Analisando...')
#r = n % 4 # % usa o resto da divisão
sleep(1)
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('{} é um ano bissexto.'.format(n))
else:
    print('{} não é um ano bissexto.'.format(n))
