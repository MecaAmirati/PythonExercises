price = float(input('Qual o preço do produto? R$'))
formaPag = int(input('(Digite 1 para pagamento com dinheiro ou 2 para pagamento com cartão)\nQual a forma de pagamento? '))
if formaPag == 2:
    numPag = int(input('Gostaria de pagar em quantas parcelas? '))
    if numPag == 1:
        descCard = price - (price*0.05)
        print('O produto que custa R${:.2f} ganha um desconto de 5% com pagamento em parcela única e passa a custar R${:.2f}'.format(price, descCard))
    elif numPag == 2:
        print('O produto terá duas parcelas fixas de R${}'.format(price/2))
    elif numPag >= 3:
        print('O produto que custa R${:.2f} terá juros de 20% e {} parcelas fixas de R${:.2f}'.format(price, numPag, ((price + (price*0.2))/numPag)))
elif formaPag == 1:
    descVist = price - (price*0.1)
    print('O produto que custa R${:.2f} ganha um desconto de 10% com pagamento à vista e passa a custar R${:.2f}'.format(price, descVist))
else:
    print('\033[030;041mERRO!\033[m\n\033[030;041mForma de pagamento inválida!\033[m')
