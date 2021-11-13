termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
print('Os 10 primeiros termos da Progressão Aritmética são:\n')

for c in range(termo, decimo + razao, razao):
    termo += razao
    print('{} '.format(c), end='→ ')
print('END')
