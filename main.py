from Card import Card
from Minion import Minion
def main():
    deck = []
    cards = open("Cards.txt", "r")
    for card in cards:
        cardInfo = card.split(',')
        nameofcard = cardInfo[0]
        costofcard = cardInfo[1]
        if len(cardInfo) == 2:
            cardData = Card(nameofcard, costofcard)
        if len(cardInfo) == 4:
            cardattack = cardInfo[2]
            cardhp = cardInfo[3]
            cardData = Minion(nameofcard, costofcard, cardattack, cardhp)
        deck.append (cardData)
    cards.close()
    for card in deck:
        card.printCard()
        print("\n")
if __name__ == "__main__":
    main()