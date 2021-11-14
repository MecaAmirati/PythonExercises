s = str(input('Digite seu sexo biológico [ M | F] : ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Digite seu sexo biológico [ M | F] :')).strip().upper()[0]
print('{} registrado com sucesso.'.format(s))
