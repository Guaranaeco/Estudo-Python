soma = 0 # Varíavel soma para usar dentro do laço


for c in range (1, 7): # Laço de 1 a 6
    num = int(input(f'Digite o {c}º número inteiro: ')) # Dentro do laço, usuário digitará 6 números inteiros
    if num % 2 == 0: # Condição analisando se os número são pares, caso sejam:
        soma += num # Será feito a soma de todos números pares digitados.

print(soma) # Resultado