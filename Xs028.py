import random
from time import sleep
#from random import randint
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
adv = int(input('Descubra qual número: '))
n = random.randrange(5)
print('analisando......\n')
sleep(2)
if (n == adv):
     print('Você acertou, Sherlock!')
else:
    print('Você errou, tente outra vez...')
print('Eu pensei no número {}. '.format(n))
