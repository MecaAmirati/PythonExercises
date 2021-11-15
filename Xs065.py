menorValor = maiorValor = 0
total = media = contador = 0
continuar = 'S'
while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    total += n
    contador += 1
    if contador == 1:
        maiorValor = menorValor = n
    else:
        if n > maiorValor:
            maiorValor = n
        if n < menorValor:
            menorValor = n
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = total / contador
print('A média entre os valores digitados é {}'.format(media))
print('O maior valor digitado foi {} e o menor foi {}'. format(maiorValor, menorValor))
