p = c = t = 0
while p != 999:
    p = int(input('Digite um valor [Digite 999 para parar]: '))
    if p < 999:
        c += 1
        t += p
print('Você digitou {} números e a soma deles é {}.'.format(c, t))
