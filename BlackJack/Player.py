class Player():
    def __init__(self,name,coins):
        self.name = name
        self.coins = coins
        self.betAmount = 0
        self.cards = []

    def Hit(self,deck):
        if len(deck) > 0:
            self.cards.append(deck.pop())
        #needs check to total value of the all the cards inthe players hand 

    def Stay(self):
        #go to dealers turn
        pass

    def points(self):
        points = 0
        for card in self.cards:
            points += card.value()
        return points