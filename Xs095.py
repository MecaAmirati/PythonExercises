jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = ' '
    while r not in 'SN':
        r = str(input('Continuar [S/N]? ')).strip().upper()
    if r == 'N':
        break
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print(f'\nO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   -> Na partida {i}, fez {v} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s)')
while True:
    busca = int(input('Mostrar detalhes de qual jogador? (999 encerra) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código {busca}')
    else:
        print(f'-- DADOS DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
print('end.')
