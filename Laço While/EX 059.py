v1 = int(input('Digite o primeiro valor: ')) # Primeiro valor
v2 = int(input('Digite o segundo valor: ')) # Segundo valor 
usuario = ''

while usuario != '5': # Enquanto o valor de usuário for diferente de 5, o programa apresenta o menu a seguir: 
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    
    usuario = str(input('Por favor, escolha uma das opções acima:  ')) # Valor do usuário
    print(' --------------------------------------------------------------')
    if usuario == '1': # Caso usuário escolha 1, soma dos valores digitados
        print(f'A soma entre os dois valores é {v1 + v2}')
    
    elif usuario == '2': # Caso usuário escolha 2, multiplicação dos valores digitados
        print(f'A multiplicação entre os dois valores é {v1 * v2}')
    
    elif usuario == '3': # Caso usuário escolha 3, pega o maior número digitado
        maior = v1
        if v2 > maior:
            maior = v2
        print(f'O maior número entre os dois valores digitados é {maior}')
    
    elif usuario == '4': # Caso usuário escolha 4, pode digitar novos números
        v1 = int(input('Por favor, digite um novo número: '))
        v2 = int(input('Por favor, digite um novo número: '))
    
    elif usuario == '5': # Saindo do programa
        print('programa encerrado')

    else: 
        print('Digite um valor válido.')
    
