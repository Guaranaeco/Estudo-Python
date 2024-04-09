soma = 0
cont = 0

while True:
    n = int(input('Digite um número (999 encerra o programa: )'))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Soma {soma}\n'
      f'Qtde {cont}')