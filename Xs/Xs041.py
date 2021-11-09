nasc = int(input('Digite o ano em que você nasceu: '))
from datetime import date
idade = (date.today().year - nasc)
print('O atleta tem {} anos e está na categoria:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade >= 25:
    print('MASTER')
