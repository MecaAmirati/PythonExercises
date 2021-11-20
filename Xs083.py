exp = str(input('Digite uma expressão com parênteses: '))
parenteses = []
for simb in exp:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Sua expressão está correta.')
else:
    print('Você não fechou todos os parênteses corretamente.')
