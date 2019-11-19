class WinnerCheck():
    #player win = 0
    #dealer win = 1
    #dealer needs to hit = 2
    #push = 3
    returnThis = 0

    def PlayerWinnerCheck(self,dealer,player):
        #check for bust
        if player.points() == 21 and dealer.points() == 21:
            #push
            self.returnThis = 3
        elif player.points() == 21:
            #Player Wins
            self.returnThis = 0
        elif player.points() > 21:
            #Dealer Wins
            self.returnThis = 1
        elif dealer.points() == player.points():
            #Push ?
            if dealer.points() < 16:
                #Dealer Hit
                self.returnThis = 2
            else:
                #Push
                self.returnThis = 3
        elif dealer.points() == 21:
            #Dealer Wins
            self.returnThis = 1
        elif dealer.points() > 21:
            #Player Wins
            self.returnThis = 0
        elif dealer.points() <= player.points():
            #Dealer Hit
            self.returnThis = 2
        elif dealer.points() > player.points():
            #Dealer Wins
            self.returnThis = 1
        else:
            print(f'Error Here are the points : {dealer.points()}, {player.points()}')
        
        return self.returnThis

