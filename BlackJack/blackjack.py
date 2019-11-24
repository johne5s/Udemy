import os
import Card
import Player
import Dealer
import DrawBoard
import WinnerCheck
import MyFunctions
from random import randint


clear = lambda: os.system('cls') #on Windows System
clear()

MyFunctions.WelcomeMsg()

#create the first deck
deck = MyFunctions.Deck()
#create the dealer
dealer = Dealer.Dealer()


#print(f'{player.name} has {player.coins} coins')


def main(deck):

    #Create the player
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
            player = Player.Player(name=pname,coins=50)
            break


    while True:
        result = MyFunctions.newDeal(player)
        if result == 2:
            return False
        else:
            if len(deck) < 20:
                #if the deck is running low on cards,  lets reshuffle the deck
                deck = MyFunctions.Deck()
            MyFunctions.NewGame(dealer,player)
            if player.coins <= 0:
                #player is out of money :(
                print(f"{player.name} has no more coins. GAME OVER")
                return False
            else:
                Main_Game(dealer,player,deck)
    
## Main Game Loop ##
def Main_Game(dealer,player,deck):
    #Ask the player for a bet
    while True:
        try:
            result = MyFunctions.GetBetAmount()
        except:
            print("Generic Error")
            continue
        else:
            if result > 0 and result <= player.coins:
                player.betAmount = result
                break

    # Give cards to player and Dealer
    player.Hit(deck)
    dealer.Hit(deck)
    player.Hit(deck)
    dealer.Hit(deck)

    #Display the cards
    clear()
    drawboard = DrawBoard.Drawboard()
    drawboard.DrawBoard(dealer,player,True)

    while True:
        #Ask to Hit, Stay or Double Down
        hitOrStay = MyFunctions.HitOrStay()
        if hitOrStay == 1:
            #player wants a card, lets give them one and refresh the board
            player.Hit(deck)
            clear()
            drawboard.DrawBoard(dealer,player,True)
            #check if the player has busted
            if player.points() > 21:
                player.coins -= player.betAmount
                print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
                print(f'{player.name} now has {player.coins} coins')
                MyFunctions.PlaySound('loss')
                break
        elif hitOrStay == 2:
            #dealers turn
            #MyFunctions.DealersTurn(dealer,player)
            while True:
                check = WinnerCheck.WinnerCheck().PlayerWinnerCheck(dealer,player)
                if check == 0:
                    #Player wins
                    clear()
                    drawboard.DrawBoard(dealer,player,False)
                    player.coins += player.betAmount
                    print(f'\n{player.name} Wins : {dealer.points()}, {player.points()}')
                    MyFunctions.PlaySound('win')
                    return False
                elif check == 1:
                    clear()
                    drawboard.DrawBoard(dealer,player,False)
                    player.coins -= player.betAmount
                    print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
                    MyFunctions.PlaySound('loss')
                    #Dealer wins
                    return False
                elif check == 2:
                    #dealer needs a card, lets give him one
                    dealer.Hit(deck)
                    continue
                elif check == 3:
                    #dealer wants to PUSH
                    print(f'\nPush : {dealer.points()}, {player.points()}')
                    MyFunctions.PlaySound('push')
                    return False
        elif hitOrStay == 3:
            #Double Down
            pass
        else:
            break
    print("complete Play again?")

if __name__ == "__main__":
    main(deck)
