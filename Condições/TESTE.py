n = 0 # N inicia com 0, quando entrar no laço recebe o valor de 1
p = n * (n + 1) / 2 # Resolvendo o mistério do scooby doo

for c in range(1, 100, 1): # Alcance do 1 ao 100 usando laço
    n += 1 # aumentando o valor de n de 1 em 1 (n=1, n=2, n=3... assim)
    p = n * (n + 1) / 2 # Calculando o valor de P:     p = 1 * (1 + 1) / 2 --------- p = 2 * (2 + 1) / 2... etc

print(p) # Mostrando apenas o resultado n°100