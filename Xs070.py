tot = valorAlto = baixoValor = 0
baixoNome = ' '
while True:
    nomeProduto = str(input('Digite o nome do produto: '))
    valor = float(input('Preço: R$'))
    tot += valor
    if baixoValor == 0 or valor < baixoValor:
        baixoValor = valor
        baixoNome = nomeProduto
    if valor > 1000:
        valorAlto += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar mais produtos? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nO total foi {tot:.2f}')
print(f'{valorAlto} itens custam mais de R$1000!')
print(f'O nome do produto mais barato é {baixoNome} que custa R${baixoValor:.2f}.')
