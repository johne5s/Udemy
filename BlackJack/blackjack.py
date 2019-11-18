import os
import sys
import time
import math
import Card
import Player
from random import randint

clear = lambda: os.system('cls') #on Windows System
clear()



def Deck():
    cardRank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardSuite = ["C","D","H","S"]
    deck = []
    for suite in cardSuite:
        for rank in cardRank:
            Card.Card(rank=rank,suite=suite)
            deck.append(Card.Card(rank=rank,suite=suite))
    
    from random import shuffle
    shuffle(deck)
    return deck

def DrawBoard():
    #dealer hand needs to be added
    clear()
    print("\nPlayer Cards")
    for card in player.cards:
        print(f'___\n|{card.rank}|\n\033[4m|{card.suite}|\033[0m')

#card = Card(rank='J',suite='D')
#print(f'{card.rank}{card.suite} : {card.value()}')

while True:
    try:
        #code to be attempted
        pname = str(input("Please provide your name: "))
        pname = pname.strip()
        if len(pname)==0 :
            continue
    except TypeError:
        print("A TypeError was found")
        continue 
    except:
        print("Generic Error")
        continue
    else:
        # No error so do the else
        # lets create the player
        player = Player.Player(name=pname,coins=50)
        break

print(f'{player.name} Has {player.coins} coins')

deck = Deck()
#print(deck[0].rank + deck[0].suite)

# Player needs to bet
while True:
    try:
        #Ask the user to Hit or Stay
        result = int(input("How much to bet?"))
    except:
        print("Not an int")
        continue
    else:
        # No error so do the else
        break

# Hit or Stay
player.Hit(deck)
player.Hit(deck)
print(f'{player.name} has been given 2 cards')

print(DrawBoard())

while True:
    try:
        #Ask the user to Hit or Stay
        result = int(input("Press 1 to Hit /nPress 2 to Stay : "))
    except:
        print("Not an int")
        continue
    else:
        # No error so do the else
        if result == 1:
            player.Hit(deck)
            DrawBoard()
        else:
            #computer's turn
            break



