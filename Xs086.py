tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        tabela[linha][coluna] = int(input(f'Valor de [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{tabela[linha][coluna]:^5}]', end='')
    print()
