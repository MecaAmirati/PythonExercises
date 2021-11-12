num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} ..............\n'.format(num))
print('O número tem {} unidade(s)'.format(u))
print('O número tem {} dezena(s)'.format(d))
print('O número tem {} centena(s)'.format(c))
print('O número tem {} milhar(es)'.format(m))
