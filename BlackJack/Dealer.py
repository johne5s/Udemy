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
            if card.rank == 'A':
                if points + 11 < 22:
                    points += 11
                else:
                    points += 1
            else:
                points += card.value()
        return points