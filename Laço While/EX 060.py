n = int(input('Digite um número: '))
contador = n
fatorial = 1
while contador > 0:
    print(f'{n}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)