from time import sleep

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo  segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
print('Analisando possibilidade de formar um triângulo e o tipo......\n')
sleep(1)

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('É possível formar um triângulo equilátero.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('É possível formar um triângulo isósceles.')
    else:
        print('É possível formar um triângulo escaleno.')
else:
    print('Não é possível formar um triângulo!')
