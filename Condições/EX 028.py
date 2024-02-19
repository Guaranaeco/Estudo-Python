from random import randint
#from time import sleep


print('Descubra o número que irei pensar... caso você acerta, receberá um prêmio!!.... valendo')
computador = randint(0, 5)
jogador = int(input('Digite um número: '))
print('Estou pensando...')


if jogador == computador:
    print('Parabéns!! Você adivinhou. ')
else:
    print(f'Você errou... que pena! meu número escolhido foi {computador}')
