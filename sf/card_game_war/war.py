class Card():
    def __init__(self, suit, rank, simple_strength_value) -> None:
        self.suit = suit
        self.rank = rank
        self.simple_strength_value = simple_strength_value 
        self.shorthand = f'{self.suit[0]}{self.rank}'

    def __str__(self) -> str:
        return self.shorthand

class Deck():
    def __init__(self) -> None:
        self.c2 = Card('club', '2', 2)
        self.c3 = Card('club', '3', 3)
        self.c4 = Card('club', '4', 4)
        self.c5 = Card('club', '5', 5)
        self.c6 = Card('club', '6', 6)
        self.c7 = Card('club', '7', 7)
        self.c8 = Card('club', '8', 8)
        self.c9 = Card('club', '9', 9)
        self.ct = Card('club', '10', 10)
        self.cj = Card('club', 'J', 11)
        self.cq = Card('club', 'Q', 12)
        self.ck = Card('club', 'K', 13)
        self.ca = Card('club', 'A', 14)
        self.d2 = Card('diamond', '2', 2)
        self.d3 = Card('diamond', '3', 3)
        self.d4 = Card('diamond', '4', 4)
        self.d5 = Card('diamond', '5', 5)
        self.d6 = Card('diamond', '6', 6)
        self.d7 = Card('diamond', '7', 7)
        self.d8 = Card('diamond', '8', 8)
        self.d9 = Card('diamond', '9', 9)
        self.dt = Card('diamond', '10', 10)
        self.dj = Card('diamond', 'J', 11)
        self.dq = Card('diamond', 'Q', 12)
        self.dk = Card('diamond', 'K', 13)
        self.da = Card('diamond', 'A', 14)
        self.h2 = Card('heart', '2', 2)
        self.h3 = Card('heart', '3', 3)
        self.h4 = Card('heart', '4', 4)
        self.h5 = Card('heart', '5', 5)
        self.h6 = Card('heart', '6', 6)
        self.h7 = Card('heart', '7', 7)
        self.h8 = Card('heart', '8', 8)
        self.h9 = Card('heart', '9', 9)
        self.ht = Card('heart', '10', 10)
        self.hj = Card('heart', 'J', 11)
        self.hq = Card('heart', 'Q', 12)
        self.hk = Card('heart', 'K', 13)
        self.ha = Card('heart', 'A', 14)
        self.s2 = Card('spade', '2', 2)
        self.s3 = Card('spade', '3', 3)
        self.s4 = Card('spade', '4', 4)
        self.s5 = Card('spade', '5', 5)
        self.s6 = Card('spade', '6', 6)
        self.s7 = Card('spade', '7', 7)
        self.s8 = Card('spade', '8', 8)
        self.s9 = Card('spade', '9', 9)
        self.st = Card('spade', '10', 10)
        self.sj = Card('spade', 'J', 11)
        self.sq = Card('spade', 'Q', 12)
        self.sk = Card('spade', 'K', 13)
        self.sa = Card('spade', 'A', 14)
        # a deck (list) of card classes
        self.full_deck  = [self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.ct,self.cj,self.cq,self.ck,self.ca]
        self.full_deck += [self.d2,self.d3,self.d4,self.d5,self.d6,self.d7,self.d8,self.d9,self.dt,self.dj,self.dq,self.dk,self.da]
        self.full_deck += [self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.ht,self.hj,self.hq,self.hk,self.ha]
        self.full_deck += [self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.st,self.sj,self.sq,self.sk,self.sa]

    def print_full_deck(self) -> list:
        li = []
        for card in self.full_deck:
            li.append(card.shorthand)
        return li

    def __str__(self) -> str:
        li = ''
        for card in self.full_deck:
            li = li + card.shorthand + ' '
        return li
        
deck = Deck()
print(deck)