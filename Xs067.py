while True:
    n = int(input('\nDigite o valor de qual tabuada quer saber: '))
    if n == 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Encerrando...')
