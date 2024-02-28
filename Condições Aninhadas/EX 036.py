valor_casa = float(input('Valor da casa: R$ ')) # Variável que recebe valor do usuário
salario = float(input('Seu salário: R$ ')) #Variável que recebe valor do usuário
tempo = int(input('Em quantos anos quer pagar? '))  #Variável que recebe valor do usuário

parcela =  valor_casa / (tempo * 12) # Variável valor mensal a se pagar (tempo * 12 para saber a quantidade de meses)
salario2 = salario * 0.30 # Váriavel salvando 30% do salário do usuário

print(f'Seu salário: R$ {salario:.2f}\n' #Apresentação dos dados
      f'Valor da casa: R$ {valor_casa:.2f}\n' #Apresentação dos dados
      f'Valor da prestação {parcela:.2f}') #Apresentação dos dados

if parcela > salario2: #Condição para avaliar se o valor da prestação excede 30% do salário do usuário.
    print('O valor da prestação mensal excede 30% seu salário, empréstimo negado') 

else: #Caso a primeira condição não seja verdadeira, a prestação é menor que 30% do salário do usuário.
    print('Empréstimo Aprovado')