distancia = int(input('Qual a distância da sua viagem? '))
viagem_longa = 0.45
viagem_curta = 0.50

if distancia <= 200:
    print(f'O valor dá sua viagem é R${viagem_curta * distancia}')
else:
    print(f'Viagem longa tem desconto :D, valor da viagem: R${viagem_longa * distancia}')