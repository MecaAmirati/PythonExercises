num = int(input('Digite um número: '))
total = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        total += 1
    else:
        print('\033[34m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} é divisível por {} números!'. format(num, total))
if total == 2:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))
