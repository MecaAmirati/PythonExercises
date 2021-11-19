valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'\nO maior valor é {max(valores)} na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor é {min(valores)} na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
