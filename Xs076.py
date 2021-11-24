import numbers
lista = ('MONITOR, 35, 165Hz, CURVED', 1636.73,
         'MOTHERBOARD, AORUS ELITE, LGA 1151, DDR4', 614.32,
         'CPU, i5-9600KF, 3.7GHz (MAX 4.6GHz)', 1559.88,
         'WATERCOOLER, MASTERLIQUID LITE 120', 288.12,
         'HD SEAGATE, 2TB, 3.5, SATA', 423.02,
         'GPU, RADEON RX 5700 XT GAMING X, 8GB', 2651.28,
         'MEM, HYPERX FURY RGB, 32GB, 2666MHz', 971.90,
         'POWER SUPPLY, 750W, CX750', 522.40,
         'SSD KINGSTON, A2000, 250GB, M.2 NVME', 339.90,
         'NOBREAK, 800VA', 420.56)
total = 0
print('-'*60)
print(f'{"COMPUTER": ^60}')
print('-'*60)
for n in lista:
    if isinstance(n, numbers.Number):
        total += n
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<50}', end='')
    else:
        print(f'R${lista[pos]:>8.2f}')
print(f'\n{"TOTAL":.<50}R${total:>8.2f}')
print('_'*60)
