media = 0 # Média idade
velhice = 0 # Idade homem mais velho
homem = '' # Nome homem mais velho
mulheres = 0 # Mulheres < 20 anos

for c in range (1 , 5): 
    nome = str(input('Digite seu nome: ')) # Nome das pessoas
    idade = int(input('Digite sua idade: ')) # Idade das pessoas
    sexo = str(input('Digite seu sexo M ou F: ')).upper() # Sexo das pessoas
    media += idade # Média de idade do grupo
    print('-----------------------------------------------------')
    if idade > velhice and sexo == 'M': # Descobrindo idade do mais velho e atribuindo o nome correspondente
        velhice = idade
        homem = nome

    elif idade < 20 and sexo == 'F': # Descobrindo quantas mulheres com menos de 20 anos tem no grupo.
        mulheres += 1

print(f'Nome do homem mais velho: {homem}')
print(f'Média de idade do grupo: {media / 2}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres}')