c = h = m = 0
s = r = ' '
while True:
    n = int(input('Idade: '))
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if n >= 18:
        c += 1
    if s == 'M':
        h += 1
    if s == 'F' and n < 20:
        m += 1
    while r not in 'SN':
        r = str(input('Continuar [S/N]?' )).strip().upper()[0]
    if r == 'N':
        break
print(f'\n{c} Usuários cadastrados são maiores de idade.')
print(f'{h} Homens foram cadatrados.')
print(f'{m} Mulheres cadastradas tem menos de 20 anos.\n')
