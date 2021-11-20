lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
lista.sort(), par.sort(), impar.sort()
print(f'\nCompleta: {lista}')
print(f'Par: {par}')
print(f'Ímpar: {impar}')
