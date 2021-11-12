alt = float(input('Digite a altura em metros da parede: '))
lar = float(input('Digite a largura em metros da parede: '))
are = alt * lar
tin = are / 2
print('A parede tem uma área de aproximadamente {:.2f}m² irá precisar de aproximadamente {:.2f} litros de tinta.' .format(are, tin))
