from random import choice # Biblioteca random, para escolhas aleatórias
from time import sleep # Biblioteca time, para pausas entre os textos

lista = ['pedra', 'papel', 'tesoura'] # Lista com as possiblidades do jokenpô
computador = choice(lista).lower() # Computador usando biblioteca random (choice) para escolher entre os 3 itens da lista, de forma aleatória
nome = str(input('Digite seu nome: ')) # NOME

print('*---*'*20) # Pular linhas
print('\033[0;31mVamos jogar JO KEN PÔ???\033[m') # Texto + cor
sleep(1)
print('\033[4;31mPrepare-se para perder! HAHAHA\033[m') # Texto + cor
print('*---*'*20)

jogador = str(input('\033[0;34mQual você escolhe? Pedra? Papel? ou Tesoura?:\033[m ')).lower() # Jogador deve escolher se joga pedra, papel ou tesoura (necessário escrever)

sleep(1)
print('\033[0;31m1')
sleep(1)
print('2')
sleep(1)
print('3')
sleep(1)
print('\033[4;31mVALENDO!\033[m')
print('*---*'*20)
sleep(1)

print(f'\033[0;31mINTEL11000K:\033[m {computador} \n' # mostrando a escolha do computador
      f'\033[0;34m{nome}:\033[m {jogador}') # mostrando a escolha do jogador

if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel': # verificação para vitória do jogador
    print('\033[0;35mDroga... parece que você ganhou!\033[m')

elif jogador =='pedra' and computador == 'pedra' or jogador == 'papel' and computador == 'papel' or jogador == 'tesoura' and computador == 'tesoura': # verificação para empate
    print('\033[4;31;40mHA! parece que empatamos... isso não é uma despedida.\033[m')

elif computador == 'pedra' and jogador == 'tesoura' or computador == 'papel' and jogador == 'pedra' or computador == 'tesoura' and jogador == 'papel': # verificação para vitória do computador
    print('')
    print('INTEL1100K está digitando...')
    sleep(1)
    print('digitando...')
    sleep(1)
    print('...')
    sleep(2)
    print('')
    print('\033[7;31;40mVENCI HAHA... loooooser!\033[m')

else:
    print('Essa opção não existe no Jokenpo, tente novamente')