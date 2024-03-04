from datetime import date

maior = 0
menor = 0

for c in range(1, 8): # Laço 1 a 7
    nascimento = int(input(f'{c}º pessoa - ano de nascimento: ')) # Usuário informar 7 datas de nascimento.
    idade = date.today().year - nascimento # calculando idade
    if idade >= 18:
        maior += 1 # Somando maiores de idade
    else:
        menor += 1 # Somando menores de idade 
        
print(f'{maior} são maiores de idade') # Resultado
print(f'{menor} são menores de idade') # Resultado