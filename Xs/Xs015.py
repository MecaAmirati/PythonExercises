d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos kilometros você andou com o carro? '))
vd = d * 60
vkm = km * 0.15
vpag = vd + vkm
print('\n')
print('O valor referente as diárias é R${:.2f}'.format(vd))
print('O valor referente a kilometragem é R${:.2f}'.format(vkm))
print('O valor total a pagar é R${:.2f}' .format(vpag))
