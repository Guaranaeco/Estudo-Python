from random import randint
class Herois:
    def __init__(self, vida, mana, ataque) -> None:
        self.vida = vida
        self.mana = mana
        self.ataque = ataque
        

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
