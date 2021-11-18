from random import randint
ranNum = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'\nNúmeros Sorteados: ', end='')
for n in ranNum:
    print(f'{n} ', end='')
print(f'\nMaior: {max(ranNum)}')
print(f'Menor: {min(ranNum)}')
