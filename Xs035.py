from time import sleep

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo  segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
print('Analisando possibilidade de formar um triângulo......')
sleep(1)

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Um triângulo é possível!')
else:
    print('Não é possível formar um triângulo!')
