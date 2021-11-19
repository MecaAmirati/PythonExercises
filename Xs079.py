n = lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor repetido.')
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(f'{lista}')
