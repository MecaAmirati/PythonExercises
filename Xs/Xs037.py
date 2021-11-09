n = int(input('Digite o número inteiro que deseja converter: '))
base = int(input('\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha uma base de conversão: '))
if base == 1:
    print('{} convertido para a base binária é {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('{} convertido para a base octal é {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('{} convertido para a base hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('\033[0;30;41mOpção inválida.\033[m')
