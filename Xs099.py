from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analisando...')
    for valor in num:
        print(f'{valor}  ', end='')
        sleep(.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Os valores são {cont}')
    print(f'O maior é {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
