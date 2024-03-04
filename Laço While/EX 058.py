from random import randint

computador = randint(0, 10) # Número aleatório fixo de 1 a 10
tentativas = 0 # Soma para tentativas

print('Tente adivinhar o número de 1 a 10') # Texto inicial
jogador = ''

while jogador != computador: # Enquanto o palpite do jogador for diferente do número do computador: 
    tentativas += 1 # Somando tentativas
    jogador = int(input('Digite um novo valor: '))
    if jogador < computador:
        print('mais...')
    elif jogador > computador:
        print('menos....')
    
print(f'Finalmente! você acertou depois de {tentativas} palpites')