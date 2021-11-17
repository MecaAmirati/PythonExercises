val = int(input('\nQual valor deseja sacar: R$'))
print('=' * 30)
ced = 100
tot = val
totCed = 0
while True:
    if tot >= ced:
        tot -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCed = 0
        if tot == 0:
            break
print('=' * 30)
