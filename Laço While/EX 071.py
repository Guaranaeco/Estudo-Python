valor = int(input('Digite o valor do saque: '))
nota = 50
contnota = 0
totalnota = valor

while True:
    if totalnota >= nota:
        totalnota -= nota
        contnota += 1
    else:
        if contnota > 0:
            print(f'Voce recebeu {contnota} de {nota}')
            contnota = 0
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        if nota == 0:
            break