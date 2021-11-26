from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Nº da Carteira de Trabalho [digite 0 caso não tenha]: '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] +35) - datetime.now().year)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
