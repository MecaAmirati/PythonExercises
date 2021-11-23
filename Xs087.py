tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        tabela[linha][coluna] = int(input(f'Valor de [{linha}, {coluna}]: '))
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{tabela[linha][coluna]:^5}]', end='')
        if tabela[linha][coluna] % 2 == 0:
            somaPar += tabela[linha][coluna]
    print()
print(f'\nSoma dos valores pares: {somaPar}')
for linha in range(0, 3):
    somaColuna += tabela[linha][2]
print(f'Soma da terceira coluna: {somaColuna}')
for coluna in range(0, 3):
    if coluna == 0 or tabela[1][coluna] > maior:
        maior = tabela[1][coluna]
print(f'Maior valor da segunda linha: {maior}')
