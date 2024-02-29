from time import sleep

print('A contagem regressiva vai começar!!!') # Texto

for c in range(10, -1, -1): # Laço de contagem regressiva, começando do 10 até o 0, diminuindo de 1 em 1.
    print(c) # Mostrando o laço diminuindo (10, 9, 8...)
    sleep(1) # Pausa de 1 segundo entre cada laço
print('Feliz ano novo!!!') # Texto fora da identação (quando terminar o laço no 0, vem para fora)