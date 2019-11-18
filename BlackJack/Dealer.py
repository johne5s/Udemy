class Dealer():
    def __init__(self):
        self.cards = []
        #print("dealer was created")

    def Hit(self,deck):
        self.cards.append(deck.pop())

    def Stay(self):
        pass

    def points(self):
        points = 0
        for card in self.cards:
            points += card.value()
        return points