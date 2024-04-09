brasileirao = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo','Fluminense', 'Fortaleza',
               'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'São Paulo', 'Vasco da Gama', 'Chapecoense')
print('Os cinco primeiros times são: ')
for time in brasileirao[0:5]:
    print(time, end=' - ')

len(brasileirao[-1])
print(f'\nO ultimo time da tabela é {brasileirao[-1]}')