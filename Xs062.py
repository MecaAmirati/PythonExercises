print('\nProgressão Aritmética\n')
primeiro = termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
maisTermos = 10
while maisTermos != 0:
    total += maisTermos
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    maisTermos = int(input('Mostrar mais quantos termos? '))
print('Você viu {} termos dessa PA.'.format(total))
