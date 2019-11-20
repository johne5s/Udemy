import os
import Card
import Player
import Dealer
import DrawBoard
import WinnerCheck
from random import randint
import playsound


clear = lambda: os.system('cls') #on Windows System
clear()

def PlaySound(clip):
    if clip == 'loss':
        playsound.playsound('sounds/loss.wav', False)
    elif clip == 'push':
        playsound.playsound('sounds/push.wav', False)
    else:
        playsound.playsound('sounds/win.wav', False)
    

def Deck():
    #creates a deck of 52 cards and returns it
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

#create the first deck
deck = Deck()
#create the dealer
dealer = Dealer.Dealer()

def NewGame(deck):
    #start a new round/new hand
    dealer.cards = []
    player.cards = []
    if len(deck) < 20:
        #if the deck is running low on cards,  lets reshuffle the deck
        deck = Deck()
    newDeal(deck)
    #Deal a new hand

while True:
    try:
        #Ask for the Players name
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

def newDeal(deck):
    hideDealerCards = True

    # Player needs to set a bet amount
    while True:
        try:
            #Ask the player for a bet amount
            result = int(input("How much to bet?"))
        except:
            print("Not an int")
            continue
        else:
            # No error so do the else
            if result > 0 and result <= player.coins:
                #don't allow 0 and less then 0 to be allowed
                #and must be lessthen or = to the amount in the bank
                player.betAmount = result
                break
            else:
                continue

    # Give cards to player and Dealer
    player.Hit(deck)
    dealer.Hit(deck)
    player.Hit(deck)
    dealer.Hit(deck)

    #Display the cards
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
                #player wants a card, lets give them one and refresh the board
                player.Hit(deck)
                clear()
                drawboard.DrawBoard(dealer,player,hideDealerCards)
                if player.points() > 21:
                    player.coins -= player.betAmount
                    print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
                    print(f'{player.name} now has {player.coins} coins')
                    PlaySound('loss')
                    break
            else:
                #show the dealers
                hideDealerCards = False

                #Check for Winner
                check = 5 # 5 is just a number higher then what will be returned later
                while check > 1:
                    check = WinnerCheck.WinnerCheck().PlayerWinnerCheck(dealer,player)
                    if check == 2:
                        #dealer needs a card, lets give him one
                        dealer.Hit(deck)
                    elif check == 3:
                        #dealer wants to PUSH
                        break
                
                clear()
                drawboard.DrawBoard(dealer,player,hideDealerCards)
                if check == 0:
                    player.coins += player.betAmount
                    print(f'\n{player.name} Wins : {dealer.points()}, {player.points()}')
                    PlaySound('win')
                    
                elif check == 3:
                    #puch, no change in money
                    print(f'\nPush : {dealer.points()}, {player.points()}')
                    PlaySound('push')
                    pass
                else:
                    player.coins -= player.betAmount
                    print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
                    PlaySound('loss')
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
