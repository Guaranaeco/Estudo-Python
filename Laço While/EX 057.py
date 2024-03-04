sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0] # Pedindo ao usuário que digite seu sexo (mais especifico M ou F)
while sexo not in 'MF': # Enquanto sexo não for M ou F, faça a ação abaixo.
    sexo = str(input('Dados inválidos, digite novamente: ')).upper().strip()[0] # Peça novamente para que o usuário digite o sexo. 
    print('----------------------------------------------------------')
print(f'Sexo {sexo} registrado com sucesso! ')