extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove' , 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n <= 0 or n > 20:
        print('meh')
        break
    print(f'Você digitou {extenso[n]}.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('meh2')
        break

'''while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print(f'Você digitou {extenso[n]}.')'''
