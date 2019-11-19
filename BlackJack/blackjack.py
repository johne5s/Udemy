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

deck = Deck()
dealer = Dealer.Dealer()

def NewGame(deck):
    dealer.cards = []
    if len(deck) < 20:
        #self.deck.clear()
        #newDeck = []
        deck = Deck()
    player.cards = []
    newDeal(deck)

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

print(f'{player.name} has {player.coins} coins')

# Create a new deck and new dealer



def newDeal(deck):
    hideDealerCards = True
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
            if result < 1:
                continue
            if result <= player.coins:
                player.betAmount = result
                break
            else:
                continue

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
                check = 5
                while check > 1:
                    check = WinnerCheck.WinnerCheck().PlayerWinnerCheck(dealer,player)
                    if check == 2:
                        dealer.Hit(deck)
                    elif check == 3:
                        break

                clear()
                drawboard.DrawBoard(dealer,player,hideDealerCards)
                if check == 0:
                    player.coins += player.betAmount
                    print(f'\n{player.name} Wins : {dealer.points()}, {player.points()}')
                elif check == 3:
                    #puch, no change in money
                    print(f'\nPush : {dealer.points()}, {player.points()}')
                    pass
                else:
                    player.coins -= player.betAmount
                    print(f'\nDealer Wins : {dealer.points()}, {player.points()}')

                print(f'{player.name} now has {player.coins} coins')
                break
    
    if player.coins <= 0:
        return None

    while True:
        try:
            #Ask the user to Hit or Stay
            result = int(input("1 = New Deal\n2 = Quit\n"))
        except:
            print("Not an int")
            continue
        else:
            if result == 1:
                NewGame(deck)
                # I don't like this
                break
            else:
                break


NewGame(deck)
