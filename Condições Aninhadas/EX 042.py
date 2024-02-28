r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('É possível formar um triângulo')
    if r1 == r2 == r3:
        print('Esse é um triângulo equilátero, todos os lados iguais')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
        print('Esse é um triângulo isósceles')
    elif r1 != r2 != r3:
        print('Esse é um triângulo Escaleno')