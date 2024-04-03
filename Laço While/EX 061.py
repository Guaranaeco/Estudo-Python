termo = int(input('Primeiro termo: ')) # Primeiro termo da PA
razao = int(input('Razao da PA: ')) # Razao da PA
limite = razao * 9 + termo # Limite de 10 termos
c = False # Verificação

while not c: # Enquanto for falso
    print(f'{termo} + {razao} = {termo + razao}') # Mostrando a soma do primeiro termo + razao
    termo += razao # Somando
    if termo > limite: # Condição de parada True
        c = True
print('PA concluida.')