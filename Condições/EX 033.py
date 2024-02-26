a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
print('-' * 10)

#Menor
menor = a 

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')