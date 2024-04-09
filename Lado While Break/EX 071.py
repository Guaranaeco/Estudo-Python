valor = int(input('Valor a ser sacado: '))
ced = 50
cedtot= 0
total = valor

while True:
    if total >= ced:
        total -= ced
        cedtot += 1
    else:
        if cedtot > 0:
            print(f'Você sacou {cedtot} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedtot = 0

        if total == 0:
            break

