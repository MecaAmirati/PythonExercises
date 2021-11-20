lista = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
lista.sort(reverse=True)
if 5 in lista:
    print(f'\nO valor 5 foi digitado.')
else:
    print('\nO valor 5 não foi digitado')
print(f'Você digitou {len(lista)} valores:')
print(f'{lista}')
