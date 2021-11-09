genero = int(input('Qual seu gênero? Digite (1) para Masculino ou (0) para Feminino: '))
if genero == 1:
    nasc = int(input('Digite o ano em que você nasceu: '))
    from datetime import date
    alist = (date.today().year - nasc)
    if alist == 18:
        print('Você precisa se alistar ainda esse ano!')
    elif alist < 18:
        print('Você ainda não tem idade para se alistar.')
        print('Você deverá se alistar em {} daqui aproximadamente {} ano(s).'.format(((18 - alist) + date.today().year), (18 - alist)))
    elif alist > 18:
        print('Você deveria ter se alistado há {} anos!'.format(alist - 18))
        print('Seu ano de alistamento foi {}!'.format(date.today().year - (alist - 18)))
else:
    print('O Serviço Militar só é obrigatório para pessoas do gênero Masculino.')
