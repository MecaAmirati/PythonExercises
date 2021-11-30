galera = list()
pessoa = dict()
cont = media = 0
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
		if pessoa['sexo'] in 'MF':
			break
		print('ERRO! Digite "M" para Masculino ou "F" pra Feminino.')
	pessoa['idade'] = int(input('Idade: '))
	cont += pessoa['idade']
	galera.append(pessoa.copy())
	r = ' '
	while r not in 'SN':
		r = str(input('Continuar [S/N]? ')).strip().upper()
	if r == 'N':
		break
print(f'\nForam cadastradas {len(galera)} pessoas')
media = cont / len(galera)
print(f'A média de idade é {media:5.5f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
	if p['sexo'] in 'Ff':
		print(f'{p["nome"]}')
print()
print('As pessoas com idade acima da média são ', end='')
for p in galera:
	if p['idade'] >= media:
		print()
		for k, v in p.items():
			print(f'{k} = {v}')
print('End')
