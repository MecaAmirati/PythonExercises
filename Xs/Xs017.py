import math
catopo = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Catero Adjacente: '))
#hip = (catopo ** 2 + catadj ** 2) ** (1/2)
print('A Hipotenusa mede {:.2f}'.format(math.hypot(catadj, catopo)))
