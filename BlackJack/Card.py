class Card():
    def __init__(self,rank,suite):
        
        # 1-10,J,Q,K,A - string
        self.rank = rank

        # (C)Clubs, (D)Diamonds, (H)Hearts, (S)Spades - string
        self.suite = suite

        # 1-11, points value - int
    def value(self):
        if self.rank.upper() == "J":
            return 10
        elif self.rank.upper() == "Q":
            return 10 
        elif self.rank.upper() == "K":
            return 10
        elif self.rank.upper() == "A":
            return 1
        else:
            return int(self.rank)