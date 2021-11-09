p = float(input('Informe o preço do produto: '))
desc = p * 0.05
pcomd = p - desc
print('O preço R${} com 5% desconto é R${:.2f} '.format(p, pcomd))
