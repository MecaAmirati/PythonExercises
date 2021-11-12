sal = float(input('Qual é o seu salário? R$'))
if sal <= 1250:
    aum = sal + (sal * .15)
    print('Seu novo salário terá um aumento de 15% e será R${:.2f}'.format(aum))
else:
    aum = sal + (sal * .1)
    print('Seu novo salário terá um aumento de 10% e será R${:.2f}'.format(aum))
