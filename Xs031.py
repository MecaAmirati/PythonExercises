dist = float(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    pas = dist * .5
    print('O preço da passagem é R${:.2f}'.format(pas))
else:
    pas = dist * .45
    print('O preço da passagem é R${:.2f}'.format(pas))
print('Tenha uma boa viagem!')
