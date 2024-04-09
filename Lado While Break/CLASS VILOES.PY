from random import randint
class Herois:
    def __init__(self, vida, mana, ataque) -> None:
        self.vida = vida
        self.mana = mana
        self.ataque = ataque
        
valor = int(input('Valor a ser sacado: '))
ced = 50
cedtot= 0
total = valor

while True:
    if total >= ced:
        total -= ced
        cedtot += 1
    else:
        if cedtot > 0:
            print(f'Você sacou {cedtot} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedtot = 0

        if total == 0:
            break


    def batalha(self, inimigo):
        inimigo.vida -= self.ataque
        chance = randint(1, 5)
        print(f'Chance de buffar... {chance}')
        if chance > 3:
            vida_extra = randint(1, 8)
            inimigo.vida += vida_extra
            print(f'Inimigo recebeu {vida_extra} de vida extra')

goku = Herois(10, 5, 5)
vegeta = Herois(10, 5, 5)



goku.batalha(vegeta)
