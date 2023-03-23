import random
import sys

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

if __name__ == '__main__':
    print_level = 1     #  <2 minimal, >=2 verbose 
    deck = Deck()       # deck contains a list of Card objects
    if print_level >= 2:
        print('new deck:')
        print(deck)
    random.shuffle(deck.full_deck)
    if print_level >= 2:
        print('shuffled deck:')
        print(deck)
    shuffled_list_of_card_objects = deck.get_deck()             
    #shuffled_list_of_card_objects = shuffled_list_of_card_objects[0:18]    # for testing
    player1_all_cards = list(shuffled_list_of_card_objects[0::2])
    player2_all_cards = list(shuffled_list_of_card_objects[1::2])
    if print_level >= 2:
        print('---')
        print(f'deck: ', end="")  
        print(*shuffled_list_of_card_objects)
        print(f'player1: ', end="")  
        print(*player1_all_cards)
        print(f'player2: ', end="")
        print(*player2_all_cards)
        print('')

    loopcount = 0
    play_game = True
    while play_game:
        if len(player1_all_cards) == 0:
            print('player 1 out of cards, player 2 wins')
            sys.exit()
            play_game = False
            break

        if len(player2_all_cards) == 0:
            print('player 2 out of cards, player 1 wins')
            sys.exit()
            play_game = False
            break

        if print_level >= 2:
            print(f'{loopcount} player1: ', end="")  
            print(*player1_all_cards)
            print(f'{loopcount} player2: ', end="")
            print(*player2_all_cards)

        # take a card from top of player's pile (list far right)
        p1_curr_card = player1_all_cards.pop()          
        p2_curr_card = player2_all_cards.pop()          

        if print_level >= 2:
            print(f'{loopcount} p1_curr_card: {p1_curr_card}, strength = {p1_curr_card.simple_strength_value}')
            print(f'{loopcount} p2_curr_card: {p2_curr_card}, strength = {p2_curr_card.simple_strength_value}')
            
        if p1_curr_card.simple_strength_value > p2_curr_card.simple_strength_value:
            # add both cards to the bottom of player's pile (list far left)
            temp = [p1_curr_card, p2_curr_card]
            # shuffle the discarded cards, never-ending game less likely
            random.shuffle(temp)    
            player1_all_cards.insert(0, temp[0])   
            player1_all_cards.insert(0, temp[1])    
        elif p1_curr_card.simple_strength_value < p2_curr_card.simple_strength_value:
            temp = [p1_curr_card, p2_curr_card]
            # shuffle the discarded cards, never-ending game less likely
            random.shuffle(temp)    
            player2_all_cards.insert(0, temp[0])   
            player2_all_cards.insert(0, temp[1])    
        else: # war! cards equal
            print("--- it's war!")
            at_war = True
            while at_war:
                repo = [p1_curr_card, p2_curr_card]
                # draw an additional 3 cards from each player in war
                if len(player1_all_cards) < 4:
                    print('player 1 out of cards, player 2 wins')
                    sys.exit()
                if len(player2_all_cards) < 4:
                    print('player 2 out of cards, player 1 wins')
                    sys.exit()
                repo.append(player1_all_cards.pop())
                repo.append(player1_all_cards.pop())
                repo.append(player1_all_cards.pop())
                p1_new_card = player1_all_cards.pop()
                repo.append(p1_new_card)
                repo.append(player2_all_cards.pop())
                repo.append(player2_all_cards.pop())
                repo.append(player2_all_cards.pop())
                p2_new_card = player2_all_cards.pop()
                repo.append(p2_new_card)
                # shuffle the discarded cards, never-ending game less likely
                random.shuffle(repo)    
                if p1_new_card.simple_strength_value > p2_new_card.simple_strength_value:
                    for c in repo:
                        player1_all_cards.insert(0, c) 
                    at_war = False
                    break
                elif p1_new_card.simple_strength_value < p2_new_card.simple_strength_value:
                    for c in repo:
                        player2_all_cards.insert(0, c) 
                    at_war = False
                    break
                else:
                    # continue war
                    if len(player1_all_cards) ==  0:
                        print('player 1 out of cards, player 2 wins')
                        sys.exit()
                    if len(player2_all_cards) ==  0:
                        print('player 2 out of cards, player 1 wins')
                        sys.exit()
                    p1_curr_card = player1_all_cards.pop()
                    p2_curr_card = player2_all_cards.pop()

        if print_level >= 2:
            print(f'{loopcount} player1: ', end="")  
            print(*player1_all_cards)
            print(f'{loopcount} player2: ', end="")
            print(*player2_all_cards)
        else:
            print(f'loop {loopcount}')

        if print_level >= 2:
            print(' ')
        loopcount += 1

    