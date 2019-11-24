class Drawboard():

    def DrawBoard(self,dealer,player,hidedealer):

        #line 0, Header
        line0 = ''
        #line 1, Top
        line1 = ''
        #line 2, Card Rank
        line2 = ''
        #line 3, Card Suite
        line3 = ''

        i=0
        d = len(dealer.cards)
        while i < d:
            if i == 1 and hidedealer == True:
                line1 += f'___ '
                line2 += f'|X| '
                line3 += f'\033[4m|X|\033[0m '
            elif dealer.cards[i].rank == '10':
                line1 += f'____ '
                line2 += f'|{dealer.cards[i].rank}| '
                line3 += f'\033[4m|{dealer.cards[i].suite} |\033[0m '
            else:
                line1 += f'___ '
                line2 += f'|{dealer.cards[i].rank}| '
                line3 += f'\033[4m|{dealer.cards[i].suite}|\033[0m '
            i+=1

        i=0
        lineLen = len(line1)+5
        while i < lineLen:
            line1 += " "
            line2 += " "
            line3 += " "
            i += 1

        for card in player.cards:
            if card.rank == '10':
                line1 += f'____ '
                line2 += f'|{card.rank}| '
                line3 += f'\033[4m|{card.suite} |\033[0m '
            else:
                line1 += f'___ '
                line2 += f'|{card.rank}| '
                line3 += f'\033[4m|{card.suite}|\033[0m '


        line0 = "\nDealer Cards "
        i=0
        while i < len(dealer.cards):
            line0 += "----"
            if i > 1:
                line0 += "----"
            i += 1
        line0 += f' {player.name}\'s cards : Bank = {player.coins} coins and is betting {player.betAmount} coins'
        print(f'{line0}\n{line1}\n{line2}\n{line3}')
