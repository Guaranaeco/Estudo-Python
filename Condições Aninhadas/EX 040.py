nota1 = float(input('Digite sua primeira nota: ')) # Primeira nota do aluno
nota2 = float(input('Digite sua segunda nota: ')) # Segunda nota do aluno
media = (nota1 + nota2) / 2 # Média das duas notas

print(media) # Verificando 

if media < 5: # Condição de reprovado, caso a nota seja menor que 5.0
    print('REPROVADO')

elif media > 7:
    print('APROVADO') # Condição de aprovado, caso a nota seja maior que 7

elif media > 4.9 and media < 7.0: # Condição de recuperação, caso a entra esteja entre 5.0 e 7.0
    print('RECUPERAÇÃO')