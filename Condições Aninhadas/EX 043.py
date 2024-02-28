peso = float(input('Qual seu peso? KG ')) # Peso do usuário
altura = float(input('Qual sua altura? ')) # altura do usuário
imc = peso / (altura * altura) # Calculando IMC do usuário

print(f'Seu IMC atual é de: {imc:.2f}') # Apresentando IMC ao usuário

if imc < 18.5: # Condição para IMC menor que 18.5
    print('Você está abaixo do peso ideal.')

elif imc <= 25: # Condição para IMC menor ou igual a 25
    print('Peso ideal')

elif imc <= 30: # Condição para IMC menor ou igual a 30
    print('Sobrepeso')

elif imc <= 40: # Condição para IMC menor ou igual a 40
    print('Obesidade')

elif imc > 40: # Condição para IMC maior que 40
    print('Obesidade mórbida')