import os
import sys
import time
import math
import Card
from random import randint

clear = lambda: os.system('cls') #on Windows System
clear()



def Deck():
    cardRank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardSuite = ["C","D","H","S"]
    deck = []
    for suite in cardSuite:
        for rank in cardRank:
            deck.append(rank+suite)
    
    from random import shuffle
    shuffle(deck)
    return deck[0]

#card = Card(rank='J',suite='D')
#print(f'{card.rank}{card.suite} : {card.value()}')

class Player():
    def __init__(self,coins,cards):
        self.coins = coins
        self.cards = cards

    def Hit(self):
        self.cards.append = deck.pop()

    def Stay(self):
        pass

class Dealer():
    def __init__(self,cards):
        self.cards = cards

    def Hit(self):
        self.cards.append = deck.pop()

    def Stay(self):
        pass


deck = Deck()
print(deck)

#def dealersHand
#def playersHand



#def DisplayBoard(dealer, player):
#    for card in dealer: 
#        print(f'{card}')
#    
#    for card in player: 
#        print(f'{card}')

