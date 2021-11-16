v = c = t = 0
while True:
    v = int(input('Digite um valor [Digite 999 para parar]: '))
    if v != 999:
        t += v
        c += 1
    else:
        break
print(f'Você digitou {c} números e a soma deles é {t}.')
