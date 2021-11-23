from random import randint
total = 1
palpites = []
jogos = []
quant = int(input('Quantos palpites quer fazer? '))
while total <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in palpites:
            palpites.append(n)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Palpite {i+ 1}: {l}')
