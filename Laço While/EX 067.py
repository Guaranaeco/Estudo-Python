while True:
    n = int(input('Digite um valor para calcular a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11, 1):
        print(f'{n} X {c} = {n * c}')
   
print('programa encerrado')