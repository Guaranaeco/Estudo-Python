t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(t, r * 10 + t, r):
    print(c, end=' ')