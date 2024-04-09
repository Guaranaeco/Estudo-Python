extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',' Dezessete', 'Dezoito', 'Dezenove', 'Vinte') # Tupla
num = int(input('Digite um número entr 0 e 20: ')) # Variável pedindo um valor

while True: # Enquanto for verdade
    
    if num >= 0 and num <= 20: # Se a variável num for maior ou igual a 0 e menor ou igual a 20, faça isso:
        print(f'Você digitou o número {extenso[num]}') # Apresente o número digitado por extenso.
        break # Pare o programa

    else: # Caso contrário
        num = int(input('Tente novamente. Digite um número entre 0 e 20: ')) # Diga para o usuário digitar algo entre 0 e 20.