times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('\n*** CAMPEONATO BRASILEIRO ***\n')
print('Ranking:\n')
contador = 0
for listaTimes in times:
    contador += 1
    print(f'{contador}º {listaTimes}')
print('\n5 primeiros colocados:\n')
lista5 = times[0:5]
contador = 0
for rank5 in lista5:
    contador += 1
    print(f'{contador}º {rank5}')
print('\nOs últimos 4 colocados:\n')
lista4ultimos = times[-4:]
contador = 16
for rank4ultimos in lista4ultimos:
    contador += 1
    print(f'{contador}º {rank4ultimos}')
print('\nLista de times em ordem alfabética:\n')
listaAlfabetica = sorted(times)
for rankAlfa in listaAlfabetica:
    print(rankAlfa)
print(f'\nPosição do time Chapecoence: {times.index("Chapecoense") + 1}ª posição.')
