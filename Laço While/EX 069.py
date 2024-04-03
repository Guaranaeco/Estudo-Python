idade18 = mulheres20 = tothomens = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if idade > 18:
            idade18 += 1
    if sexo == 'M':
            tothomens += 1
    if sexo == 'F' and idade < 20:
            mulheres20 += 1
    continuar = 'z'
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break

print(f'Total de homens: {tothomens}\n'
      f'Mulheres com menos de 20 anos: {mulheres20}\n'
      f'Homens com mais de 18 anos: {idade18}')