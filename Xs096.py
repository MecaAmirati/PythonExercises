def area(largura, altura):
    calcarea = largura * altura
    print(f'\nA área de {largura}m x {altura}m é {calcarea:.2f}m²')


a = float(input('Largura em metros: '))
b = float(input('Altura em metros: '))
area(a, b)
