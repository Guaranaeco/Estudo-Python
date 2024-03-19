n = int(input('Valor: ')) # Valor inicial
escolha = 1 # Varíavel de escolha
maior = menor = n # Varíavel menor e maior
media = 0 # Varíavel média
cont = 0 # Varíavel contador

while escolha != 0: # Enquanto escolha for diferente de 0, faça isso:  
    escolha = int(input('[0] Para sair\n' # Apresentando escolhas, 0 para sair e 1 para continuar
                        '[1] Para continuar:\n'))
    cont += 1 # Contador recebendo soma +1 a cada laço
    media += n # Média somando valores digitados.

    if escolha == 1: # Caso a escolha seja 1:
        n = int(input('Novo valor: ')) # O programa continua e pede um novo valor

    elif escolha == 0: # Caso a escolha seja 0:
        print('fim') # O programa encerra

    else: # Caso não seja nenhuma das opções acima, ele pede um valor correto..
        print('Digite um valor correto.')

    if maior < n: # Se maior for menor que N, maior recebe um novo valor (n)
        maior = n

    elif menor > n: # Se menor for menor que N, menor recebe um novo valor (n)
        menor = n

print(cont, media / cont) # Mostrando quantos números foram digitados, calculando média
print(f'O maior número é {maior}') # Mostrando maior número
print(f'O menor número é {menor}') # Mostrando menor número
