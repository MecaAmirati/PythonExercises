n = (int(input('Primeiro número = ')), int(input('Segundo número = ')),
     int(input('Terceiro número = ')), int(input('Quarto número = ')))
print(f'Sequência digitada: {n}')
print(f'Você digitou 9, {n.count(9)} vez(es)')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
for c in n:
    if c % 2 == 0:
        print(n, end=' ')
