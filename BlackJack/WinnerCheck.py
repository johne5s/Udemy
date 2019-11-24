class WinnerCheck():
    #player win = 0
    #dealer win = 1
    #dealer needs to hit = 2
    #push = 3
    

    def PlayerWinnerCheck(self,dealer,player):
        dealerPoints = dealer.points()
        playerPoints = player.points()
        returnThis = 0
        #check for bust
        if playerPoints == 21 and dealerPoints == 21:
            #push
            self.returnThis = 3
        elif playerPoints == 21:
            #Player Wins
            self.returnThis = 0
        elif playerPoints > 21:
            #Dealer Wins
            self.returnThis = 1
        elif dealerPoints == playerPoints:
            #Push ?
            if dealerPoints < 16:
                #Dealer Hit
                self.returnThis = 2
            else:
                #Push
                self.returnThis = 3
        elif dealerPoints == 21:
            #Dealer Wins
            self.returnThis = 1
        elif dealerPoints > 21:
            #Player Wins
            self.returnThis = 0
        elif dealerPoints <= playerPoints:
            #Dealer Hit
            self.returnThis = 2
        elif dealerPoints > playerPoints:
            #Dealer Wins
            self.returnThis = 1
        else:
            print(f'Error Here are the points : {dealerPoints}, {playerPoints}')
        
        return self.returnThis

