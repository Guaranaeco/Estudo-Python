soma = 0 # Variável soma para usarmos mais tarde

for c in range (1, 501, 2): # Laço do 1 ao 500, pulando de 2 em 2
    if c % 3 == 0: # Identificando multiplos de 3
        soma += c # Somando multiplos de 3
    print(c, end=' ') # Apresentando resultado

print(f'\n{soma}') # Apresentando a soma total.
print('teste')
print('teste')