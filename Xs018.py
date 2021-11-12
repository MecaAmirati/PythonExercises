import math
#from math import sin, cos, tan
ang = float(input("Digite um ângulo: "))
ang = math.radians(ang)
print('O seno desse ângulo é {:.2f}'.format(math.sin(ang)))
print('O cosseno desse ângulo é {:.2f}'.format(math.cos(ang)))
print('A tangente desse ângulo é {:.2f}'.format(math.tan(ang)))
