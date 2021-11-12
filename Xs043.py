from time import sleep
alt = float(input('Qual sua altura em centímetros? '))
peso = float(input('Qual seu peso em Kg? '))
imc = peso / ((alt/100) ** 2)
print('Analisando resultados.........\n')
sleep(1)
if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso ideal.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está com o peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} e você está obeso.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida.'.format(imc))
else:
    print(imc)
