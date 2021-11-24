boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    r = ' '
    while r not in "SN":
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print(f'\n{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opc = int(input('\nDigite o número do aluno que quer ver as notas [999 para parar]:  '))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'As notas de {boletim[opc][0]} são {boletim[opc][1]}')
