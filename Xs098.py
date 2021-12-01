from time import sleep


def crescente():
    print('Contagem de 1 a 10 de 1 em 1:')
    for cres in range(1, 11, 1):
        print(f'{cres} ', end='')
        sleep(.5)
    print('FIM')


def decrescente():
    print('\nContagem de 10 a 0 de -2 em -2:')
    for dec in range(10, -2, -2):
        print(f'{dec} ', end='')
        sleep(.5)


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    for con in range(a, b, c):
        print(f'{con} ', end='')
        sleep(.5)


print(crescente())
print(decrescente())
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
print(contador(a, b, c))
