produto = float(input('Digite o valor do produto: ')) # Valor do produto 
dinheiro = produto - (produto * 0.10) # Variável armazenando desconto de 10%
cartao = produto - (produto * 0.05) # Variável armazenando desconto de 5%
cartao_2x = produto / 2 # Variável armazenando o valor de 2 parcelas

print('1 - Á vista dinheiro/cheque, 10% de desconto. \n'  # Menu para que o usuário selecione a opção desejada
      '2 - Á vista no cartão, 5% de desconto \n'
      '3 - em até 2x no cartão, preço normal.\n'
      '4 - 3x ou mais no cartão, 20% de juros')

usuario = str(input('Por favor, digite o número da opção desejada: ')) # Após verificar o menu, usuário deve digitar um número.


#OBS: Abaixo temos '1' entre áspas, devido ao menu de escolha que está no tipo STR(STRING), e não INT (INTEIRO)

if usuario == '1': # Caso usuário escolha 1, pagamento a vista com dinheiro/cheque
    print(f'Pagamento a vista no dinheiro, o valor atual de R${produto:.2f} com 10% de desconto cai para R${dinheiro:.2f}')

elif usuario == '2': # Caso usuário escolha 2, pagamento a vista com cartão
    print(f'Pagamento a vista no cartão, o valor atual de R${produto:.2f} com 5% de desconto cai para R${cartao:.2f}')

elif usuario == '3': # Caso usuário escolha 3, está parcelando em 2x sem desconto
    print(f'Pagamento parcelado em 2x, o valor atual de R${produto:.2f}, fica duas parcelas de {cartao_2x:.2f} cada.')

elif usuario =='4': # Caso o usuário escolha 4, está parcelando em 3x + com 20% de juros.
    parcela = int(input('Em quantas vezes deseja parcelar? de 3 a 12 meses.'))
    print(f'Parabéns, você parcelou em {parcela} vezes, o valor atual do produto é {produto + (produto * 0.20):.2f} o valor de cada parcela ficará {(produto + (produto * 0.20)) / parcela}:.2f')

else:
    print('Por favor, digite uma opção válida.')