lista = ('MONITOR', 'ELITE', 'MOTHERBOARD', 'CPU',
         'MASTERLIQUID', 'SATA', 'GAMING', 'GPU',
         'HYPERX', 'FURY', 'POWER', 'KINGSTON')
for p in lista:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')
