from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(.3)
    print('End')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Soma dos valores pares dentro de {lista} é {soma}')


num = list()
sorteia(num)
somaPar(num)
