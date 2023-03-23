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

def war(repo, p1_card, p2_card):
    if p1_card.simple_strength_value > p2_card.simple_strength_value:
        repo.append(p1_card)
        repo.append(p2_card)
        winner_str = 'p1wins'
    elif p1_card.simple_strength_value < p2_card.simple_strength_value:
        repo.append(p1_card)
        repo.append(p2_card)
        winner_str = 'p2wins'
    else:
        winner_str = 'draw'
    print('war_repo: ', end="")
    print(*repo)
    return [winner_str, repo]

def check_for_winner_before_pop(p1_cards, p2_cards):
    winner_found = False
    if len(p1_cards) == 0:
            print('player 1 has no cards left, player 2 wins!')
            winner_found = True
    elif len(p2_cards) == 0:
            print('player 2 has no cards left, player 1 wins!')
            winner_found = True
    return winner_found 

if __name__ == '__main__':
    deck = Deck()       # deck contains a list of Card objects
    print('new deck:')
    print(deck)
    random.shuffle(deck.full_deck)
    print('shuffled deck:')
    print(deck)
    print('')
    shuffled_list_of_card_objects = deck.get_deck()             
    #shuffled_list_of_card_objects = shuffled_list_of_card_objects[0:21]
    player1_cards = list(shuffled_list_of_card_objects[0::2])
    player2_cards = list(shuffled_list_of_card_objects[1::2])

    battle_repo = []
    loopcount = 0
    while True:
        # take a card from top of player's pile (list far right)
        game_over = check_for_winner_before_pop(player1_cards, player2_cards)
        if game_over:
            break
        p1_card = player1_cards.pop()          
        p2_card = player2_cards.pop()          
        print(f'{loopcount} p1_card: {p1_card}, strength = {p1_card.simple_strength_value}')
        print(f'{loopcount} p2_card: {p2_card}, strength = {p2_card.simple_strength_value}')
        if p1_card.simple_strength_value > p2_card.simple_strength_value:
            # add both cards to the bottom of player's pile (list far left)
            player1_cards.insert(0, p1_card)   
            player1_cards.insert(0, p2_card)    
        elif p1_card.simple_strength_value < p2_card.simple_strength_value:
            player2_cards.insert(0, p1_card)   
            player2_cards.insert(0, p2_card)    
        else: # war!                                                  
            # add the two equal cards to the repo
            battle_repo.append(p1_card)             
            battle_repo.append(p2_card)  
            # also add another card from each player to the repo
            game_over = check_for_winner_before_pop(player1_cards, player2_cards)
            if game_over:
                break
            battle_repo.append(player1_cards.pop())
            battle_repo.append(player2_cards.pop())
            # war
            game_over = check_for_winner_before_pop(player1_cards, player2_cards)
            if game_over:
                break
            result = war(battle_repo, player1_cards.pop(), player2_cards.pop())
            war_repo = result[1]
            if result[0] == 'p1wins':
                for x in war_repo:
                    player1_cards.insert(0, x)
                battle_repo = []
            elif result[0] == 'p2wins':
                for x in war_repo:
                    player2_cards.insert(0, x)
                battle_repo = []
            elif result[0] == 'draw':
                battle_repo = result[1]
        
        #input("hit enter") 
        print(f'{loopcount} player1: ', end="")  
        print(*player1_cards)
        print(f'{loopcount} player2: ', end="")
        print(*player2_cards)
        print('repo: ', end="")
        print(*battle_repo)

        loopcount += 1

    