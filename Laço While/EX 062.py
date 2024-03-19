termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razao da PA: '))
c = 0
b = 1
while b != 0:
    print(f'{termo} ', end=' ')
    termo += razao
    c += 1
    if c == 10:
        b = int(input('Deseja ver mais quantos termos?'))
        