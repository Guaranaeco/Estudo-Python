num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1, 1):
    print(c, end=' ')
    if num % c == 0:
        cont += 1

if cont == 2:
    print(f'\nO número {num} foi dividido {cont} vezes e é número primo.')
else:
    print(f'O número {num} foi divido {cont} vezes e não é número primo.')