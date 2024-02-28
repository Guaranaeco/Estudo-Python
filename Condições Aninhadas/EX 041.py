from datetime import date
nascimento = int(input('Digite seu ano de nascimento: ')) # Ano de nascimento do usuário
ano = date.today().year # Biblioteca para pegar o ano atual (2024)
idade = ano - nascimento # Descobrindo idade do usuário
 
if idade <= 9: # Se idade for menor ou igual a 9 anos = MIRIM
    print('Sua categoria é MIRIM')

elif idade <= 14: # Se idade for menor ou igual a 14 anos = INFANTIL
    print('Sua categoria é INFANTIL')

elif idade <= 19: # Se idade for menor ou igual a 19 anos = JUNIOR
    print('Sua categoria é JUNIOR') 

elif idade == 20: # Se idade for == a 20 anos = SÊNIOR
    print('Sua categoria é SÊNIOR')

elif idade > 20: # Se idade for maior que 20 ano = MASTER
    print('Sua categoria é MASTER')   