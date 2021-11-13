from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    aniv = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - aniv
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo, tivemos {} pessoas que são maiores de idade.'.format(totalMaior))
print('Ao todo, tivemos {} pessoas que são menores de idade.'.format(totalMenor))
