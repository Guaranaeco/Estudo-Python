termo = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
limite = razao * 9 + termo
c = False
while not c:
    print(f'{termo} + {razao} = {termo + razao}')
    termo += razao
    if termo > limite:
        c = True
print('PA concluida.')