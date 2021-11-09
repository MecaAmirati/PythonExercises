n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('\033[30:41m REPROVADO \033[m')
elif med >= 5 and med < 6.9:
    print('\033[30:43m RECUPERAÇÃO \033[m')
elif med >= 7:
    print('\033[30:42m APROVADO \033[m')
