import random

class Card():
    def __init__(self, suit, rank, simple_strength_value) -> None:
        self.suit = suit
        self.rank = rank
        self.simple_strength_value = simple_strength_value 
        self.shorthand = f'{self.suit}{self.rank}'

    def __str__(self) -> str:
        return self.shorthand

class Deck():
    def __init__(self) -> None:
        self.c2 = Card('c', '2', 2)
        self.c3 = Card('c', '3', 3)
        self.c4 = Card('c', '4', 4)
        self.c5 = Card('c', '5', 5)
        self.c6 = Card('c', '6', 6)
        self.c7 = Card('c', '7', 7)
        self.c8 = Card('c', '8', 8)
        self.c9 = Card('c', '9', 9)
        self.ct = Card('c', 'T', 10)
        self.cj = Card('c', 'J', 11)
        self.cq = Card('c', 'Q', 12)
        self.ck = Card('c', 'K', 13)
        self.ca = Card('c', 'A', 14)
        self.d2 = Card('d', '2', 2)
        self.d3 = Card('d', '3', 3)
        self.d4 = Card('d', '4', 4)
        self.d5 = Card('d', '5', 5)
        self.d6 = Card('d', '6', 6)
        self.d7 = Card('d', '7', 7)
        self.d8 = Card('d', '8', 8)
        self.d9 = Card('d', '9', 9)
        self.dt = Card('d', 'T', 10)
        self.dj = Card('d', 'J', 11)
        self.dq = Card('d', 'Q', 12)
        self.dk = Card('d', 'K', 13)
        self.da = Card('d', 'A', 14)
        self.h2 = Card('h', '2', 2)
        self.h3 = Card('h', '3', 3)
        self.h4 = Card('h', '4', 4)
        self.h5 = Card('h', '5', 5)
        self.h6 = Card('h', '6', 6)
        self.h7 = Card('h', '7', 7)
        self.h8 = Card('h', '8', 8)
        self.h9 = Card('h', '9', 9)
        self.ht = Card('h', 'T', 10)
        self.hj = Card('h', 'J', 11)
        self.hq = Card('h', 'Q', 12)
        self.hk = Card('h', 'K', 13)
        self.ha = Card('h', 'A', 14)
        self.s2 = Card('s', '2', 2)
        self.s3 = Card('s', '3', 3)
        self.s4 = Card('s', '4', 4)
        self.s5 = Card('s', '5', 5)
        self.s6 = Card('s', '6', 6)
        self.s7 = Card('s', '7', 7)
        self.s8 = Card('s', '8', 8)
        self.s9 = Card('s', '9', 9)
        self.st = Card('s', 'T', 10)
        self.sj = Card('s', 'J', 11)
        self.sq = Card('s', 'Q', 12)
        self.sk = Card('s', 'K', 13)
        self.sa = Card('s', 'A', 14)
        # a deck (list) of card classes
        self.full_deck  = [self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.ct,self.cj,self.cq,self.ck,self.ca]
        self.full_deck += [self.d2,self.d3,self.d4,self.d5,self.d6,self.d7,self.d8,self.d9,self.dt,self.dj,self.dq,self.dk,self.da]
        self.full_deck += [self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.ht,self.hj,self.hq,self.hk,self.ha]
        self.full_deck += [self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.st,self.sj,self.sq,self.sk,self.sa]

    def get_deck(self):
        return self.full_deck

    def __str__(self) -> str:
        the_str = ''
        for card in self.full_deck:
            the_str = the_str + card.shorthand + ' '
        return the_str

class Player():
    def __init__(self, cards_held) -> None:
        self.cards_held = cards_held

    def __str__(self) -> str:
        the_str = ''
        for card in self.cards_held:
            the_str = the_str + card.shorthand + ' '
        return the_str

deck = Deck()       # deck contains a list of Card objects
print('new deck:')
print(deck)
random.shuffle(deck.full_deck)
print('shuffled deck:')
print(deck)
shuffled_list_of_card_objects = deck.get_deck()             
player1 = Player(shuffled_list_of_card_objects[0::2])
player2 = Player(shuffled_list_of_card_objects[1::2])
print("player1's list of card objects")
print(player1)
print("player2's list of card objects")
print(player2)
battle_repo = []
p1_card = player1.cards_held.pop() # take last card (right) from list
p2_card = player2.cards_held.pop()
print(player1)
print(player2)
print(p1_card)
print(p2_card)
player1.cards_held.insert(0,p1_card)
player2.cards_held.insert(0,p2_card)
print(player1)
print(player2)