count = 1
n = int(input('Digite o número para o programa fatorar: '))

while count < n:
    n *= count
    count += 1

print(n)