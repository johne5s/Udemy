import Card
import WinnerCheck
import playsound

def WelcomeMsg():
    print("Welcome to my card game!  Lets play 21")

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

def GetBetAmount():
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
            return result

def HitOrStay():
    while True:
        try:
            #Ask the user to Hit or Stay
            result = int(input("Press 1 to Hit \nPress 2 to Stay\nPress 3 to Double Down\n"))
        except:
            print("Not an int")
            continue
        else:
            # No error so do the else
            if result == 1 or result == 2 or result == 3:
                return result

def NewGame(dealer,player):
    #start a new round/new hand
    dealer.cards = []
    player.cards = []
    

def newDeal(player):
    while True:
        try:
            #Ask the user to Hit or Stay
            print(f"{player.name}, your bank is now {player.coins}")
            result = int(input("Press 1 to New Deal \nPress 2 to Quit : \n"))
        except:
            print("Not an int")
            continue
        else:
            if result > 0 and result < 3:
                return result



# def DealersTurn(dealer,player):
#     #Check for Winner
#     check = 5 # 5 is just a number higher then what will be returned later
#     while check > 1:
#         check = WinnerCheck.WinnerCheck().PlayerWinnerCheck(dealer,player)
#         if check == 2:
#             #dealer needs a card, lets give him one
#             dealer.Hit(deck)
#         elif check == 3:
#             #dealer wants to PUSH
#             break
    
#     clear()
#     drawboard.DrawBoard(dealer,player,False)
#     if check == 0:
#         player.coins += player.betAmount
#         print(f'\n{player.name} Wins : {dealer.points()}, {player.points()}')
#         PlaySound('win')
        
#     elif check == 3:
#         #puch, no change in money
#         print(f'\nPush : {dealer.points()}, {player.points()}')
#         PlaySound('push')
#         pass
#     else:
#         player.coins -= player.betAmount
#         print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
#         PlaySound('loss')
#     print(f'{player.name} now has {player.coins} coins')
    





    # while True:
    #     try:
    #         #Ask the user to Hit or Stay
    #         result = int(input("Press 1 to Hit \nPress 2 to Stay : \n"))
    #     except:
    #         print("Not an int")
    #         continue
    #     else:
    #         # No error so do the else
    #         if result == 1:
    #             #player wants a card, lets give them one and refresh the board
    #             player.Hit(deck)
    #             clear()
    #             drawboard.DrawBoard(dealer,player,hideDealerCards)
    #             if player.points() > 21:
    #                 player.coins -= player.betAmount
    #                 print(f'\nDealer Wins : {dealer.points()}, {player.points()}')
    #                 print(f'{player.name} now has {player.coins} coins')
    #                 PlaySound('loss')
    #                 break
            #else:
                
    
    # if player.coins <= 0:
    #     return None

    # while True:
    #     try:
    #         #Ask the user to Hit or Stay
    #         result = int(input("1 = New Deal\n2 = Quit\n"))
    #     except:
    #         print("Not an int")
    #         continue
    #     else:
    #         if result == 1:
    #             NewGame(deck)
    #             # I don't like this
    #             break
    #         else:
    #             break