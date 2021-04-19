from Card import Card

class Minion(Card):
    def __init__(self, name, cost, attack, hp):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.hp = hp

    def printCard(self):
        Card.printCard(self)
        print("Attack Points:", self.attack)
        print("Health Points:", self.hp)

