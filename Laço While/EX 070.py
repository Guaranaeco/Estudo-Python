cont = totgasto = mil = barato = 0
maiscaro = ''
while True:
    nome_produto = str(input('Nome do produto: '))
    valor_produto = float(input('Valor do produto: '))
    cont += 1
    totgasto += valor_produto
    if valor_produto > 1000:
        mil += 1
    if cont == 1:
        barato = valor_produto
    if barato > valor_produto:
        barato = valor_produto
        maiscaro = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continuar == 'N':     
        break
    

print(f'Qtde de produto com valor acima de R$1000: {mil}')
print(f'Nome do produto mais barato {maiscaro} R${barato}')
print(f'Total gasto pela compra {totgasto}')