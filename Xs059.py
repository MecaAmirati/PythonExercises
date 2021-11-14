from time import sleep
n1 = float(input('\nDigite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = 0
while op != 8:
    print('Qual operação deseja realizar com esses valores?\n')
    op = int(input('[1] Soma\n[2] Subtração\n[3] Multiplicação\n'
                   '[4] Divisão\n[5] Maior\n[6] Menor\n'
                   '[7] Digitar outros números\n[8] Sair\nOpção: '))
    if op == 1:
        soma = n1 + n2
        print('{} + {} = {}\n'.format(n1, n2, soma))
    elif op == 2:
        sub = n1 - n2
        print('{} - {} = {}\n'.format(n1, n2, sub))
    elif op == 3:
        multi = n1 * n2
        print('{} x {} = {}\n'.format(n1, n2, multi))
    elif op == 4:
        div = n1 / n2
        print('{} / {} = {:.2f}\n'.format(n1, n2, div))
    elif op == 5:
        if n1 > n2:
            print('{} é maior que {}\n'.format(n1, n2))
        if n2 > n1:
            print('{} é maior que {}\n'.format(n2, n1))
        else:
            print('{} é igual a {}\n'.format(n1, n2))
    elif op == 6:
        if n1 < n2:
            print('{} é menor que {}\n'.format(n1, n2))
        if n2 < n1:
            print('{} é menor que {}\n'.format(n2, n1))
        if n1 == n2:
            print('{} é igual a {}\n'.format(n1, n2))
    elif op == 7:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif op == 8:
        print('\nEncerrando..........')
        sleep(1)
    else:
        print('Opção Inválida. Tente novamente.')

print('\nObrigado!')
