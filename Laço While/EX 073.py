brasileirao = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
               'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Chapecoense', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print(f'O time chapecoense está na posição {brasileirao.index("Chapecoense") + 1} da tabela do brasileirão')
print(f'Os 5 primeiros do brasileirao são: {brasileirao[:5]}')
print(f'Os 4 últimos times do brasileirão são: {brasileirao[-4:]}')
print(sorted(brasileirao))
