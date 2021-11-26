from random import randint
from operator import itemgetter
jogo = {'jogador_1': randint(1, 7),
        'jogador_2': randint(1, 7),
        'jogador_3': randint(1, 7),
        'jogador_4': randint(1, 7)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
print()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
