for c in range(1 ,6):
    peso = float(input('Digite seu peso: ')) # O peso de 5 pessoas será digitado
    if c == 1:
        maior = menor = peso # Atribuindo valor inicial as variáveis "maior" "menor"

    elif peso > maior: # Verificando maior peso 
        maior = peso

    elif peso < menor: # Verificando menor peso
        menor = peso

print(maior)
print(menor)