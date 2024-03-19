from random import randint

computador = randint(0, 10)
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Adivinhe o número que pensei: '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... ')
        else:
            print('Um pouco menos...')

print('Você acertou, parabéns')