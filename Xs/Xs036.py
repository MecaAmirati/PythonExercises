valor = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar? '))
parcela = anos * 12
emprestimo = valor / parcela

print('Empréstimo no valor de {:.2f} a ser pago em {} parcela(s) de R${:.2f}...'.format(valor, parcela, emprestimo))
if emprestimo > (salario *.3):
    print("Valor do empréstimo é maior que 30% do salário.")
    print('\033[0;30;41mEmpréstimo negado.\033[m')
else:
    print('\033[0;30;42mEmpréstimo aprovado. Parabéns!\033[m')
