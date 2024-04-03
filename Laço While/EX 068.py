from random import randint

cont = 0
soma = 0

while True: # Enquanto for verdade
    computador = randint(1, 10) # Numero aleatório do computador do 1 ao 10
    numero = int(input('Qual sua jogada: ')) # Número do par ou impar
    escolha = str(input('[P/I]')).upper() # Par ou impar
    soma = numero + computador # Soma do computador + usuario
 
    if soma % 2 == 0 and escolha == 'P': # Se soma / 2 der resto 0 e escolha 'P' - usuario vence com PAR
        print(f'Você jogou {numero} e o computador {computador} a soma é {soma}')
        print('Parabéns, você ganhou... vamos novamente')

    elif soma % 2 == 1 and escolha == 'I': # Se soma / 2 der resto 1 e escolha 'I' - usuario vence com Impar
        print(f'Você jogou {numero} e o compuador {computador} a soma é {soma} DEU ÍMPAR') #

    else: # Caso as condições acima não forem atendidas, 99,99% de chance do usuario ter perdido
        print('Você perdeu!!! hahaha')
        print(f'Você jogou {numero} e eu {computador} = {soma}')
        break
