class WinnerCheck():
    didPlayerWin = True

    def PlayerWinnerCheck(self,dealer,player):
        #check for bust
        if player.points() > 21:
            print(f'Dealer Wins, player bust : {dealer.points()}, {player.points()}')
            self.didPlayerWin = False
        elif dealer.points() == 21:
            print("Dealer Wins")
            self.didPlayerWin = False
        elif dealer.points() > 21:
            print(f'Player Wins, Dealer Bust : {dealer.points()}, {player.points()}')
        elif dealer.points() < player.points():
            while dealer.points() < player.points():
                dealer.Hit()
                if dealer.points() > player.points():
                    print(f'Dealer Wins : {dealer.points()}, {player.points()}')
                    self.didPlayerWin = False
        elif dealer.points() > player.points():
            print(f'Dealer Wins : {dealer.points()}, {player.points()}')
            self.didPlayerWin = False
        else:
            print(f'Here are the points : {dealer.points()}, {player.points()}')
        
        return self.didPlayerWin

