num = int(input('Digite um número para calcularmos a tabuada: ')) # Número quer será multiplicado
tab = int(input('Digite o número até onde você quer a tabuada: ')) # Número limite da tabuada

for c  in range (1, tab + 1): # Inicio 1 - Fim, número digitado pelo usuário.
    result = num * c # Multiplicação 
    print(f'{num} * {c} = {result}') # Mostrando resultados