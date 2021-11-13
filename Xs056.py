maiorIdadeHomem = 0
totalIdades = 0
mediaIdade = 0
numjovem = 0
idoso = ''
for pessoa in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '. format(pessoa))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(pessoa)))
    sexo = str(input('Sexo [M | F]: ')).strip()
    totalIdades += idade
    mediaIdade = totalIdades / 4
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        idoso = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        idoso = nome
    if sexo in 'Ff' and idade < 20:
        numjovem += 1
print('\nA média de idade do grupo é {:.2f}.'.format(mediaIdade))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(idoso, maiorIdadeHomem))
print('Entre as mulheres, {} tem menos que 20.'.format(numjovem))
