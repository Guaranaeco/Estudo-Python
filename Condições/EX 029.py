velocidade = int(input('Velocidade do carro: '))
multa = 0
dif = velocidade - 80

if velocidade > 80:
    multa = dif * 7
    print(f'Você foi multado! o valor a ser pago é de R${multa}')
else:
    print('Está tudo bem... você não foi multado :D')