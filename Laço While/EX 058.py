from random import randint

computador = randint(0, 10) # Número aleatório
acertou = False # Condição 
tentativa = 0 # Tentativas

while not acertou: # Enquanto não acertou (Enquanto o laço for falso faça o seguinte: )
    jogador = int(input('Adivinhe o número que pensei: ')) # Jogador escolhe um número
    tentativa += 1 # Soma de tentativa
    if jogador == computador: # Condição para acerto
        acertou = True # Laço se torna True, fim.
    else:
        if jogador < computador:
            print('Um pouco mais... ')
        else:
            print('Um pouco menos...')

print('Você acertou, parabéns')