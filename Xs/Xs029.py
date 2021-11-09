vel = float(input('Qual é a velocidade do veículo em Km/h? '))
multa = (vel - 80) * 7
if multa >= 1:
    print('Você ultrapassou o limite de 80Km/h e sua multa é de R${:.2f}.'.format(multa))
else:
    print('Você está dentro da velocidade permitida.')
print('Tenha um bom dia!')
