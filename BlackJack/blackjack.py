import os
import sys
import time
import math
import Card
import Player
import Dealer
import DrawBoard
import WinnerCheck
from random import randint

clear = lambda: os.system('cls') #on Windows System
clear()

hideDealerCards = True

### Functions

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



## End Functions

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
dealer = Dealer.Dealer()
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
        player.betAmount = result
        break

# Hit or Stay
player.Hit(deck)
dealer.Hit(deck)
player.Hit(deck)
dealer.Hit(deck)

clear()
drawboard = DrawBoard.Drawboard()
drawboard.DrawBoard(dealer,player,hideDealerCards)

while True:
    try:
        #Ask the user to Hit or Stay
        result = int(input("Press 1 to Hit \nPress 2 to Stay : \n"))
    except:
        print("Not an int")
        continue
    else:
        # No error so do the else
        if result == 1:
            player.Hit(deck)
            clear()
            drawboard.DrawBoard(dealer,player,hideDealerCards)
        else:
            #show the dealers
            hideDealerCards = False
            clear()
            drawboard.DrawBoard(dealer,player,hideDealerCards)

            #Check for Winner
            check = WinnerCheck.WinnerCheck().PlayerWinnerCheck(dealer,player)

            clear()
            drawboard.DrawBoard(dealer,player,hideDealerCards)
            if check == True:
                player.coins += player.betAmount*2
            else:
                player.betAmount -= player.betAmount

            print(f'{player.name} now has {player.coins} coins')
            #Ask to keep playing

            break



