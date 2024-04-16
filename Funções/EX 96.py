def area_terreno(l, c):
    area = l * c
    print(f'A área de {largura} x {comprimento} é de {area}')

print('Controle de terreno')
print('-'*len('Controle de terreno'))
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area_terreno(largura, comprimento)