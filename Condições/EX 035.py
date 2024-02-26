r1 = int(input('Reta do primeiro triângulo: '))
r2 = int(input('Reta do segundo triângulo: '))
r3 = int(input('Reta do terceiro triângulo: '))

# Condição para um triângulo se formar, a soma de 2 retas devem ser maior que a terceira.

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Pode se formar um triângulo.')
else:
    print('Não se pode formar um triângulo com essas medidas')