import random

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
        self.cj = Card('c', 'J', 10)
        self.cq = Card('c', 'Q', 10)
        self.ck = Card('c', 'K', 10)
        self.ca = Card('c', 'A', 11)
        self.d2 = Card('d', '2', 2)
        self.d3 = Card('d', '3', 3)
        self.d4 = Card('d', '4', 4)
        self.d5 = Card('d', '5', 5)
        self.d6 = Card('d', '6', 6)
        self.d7 = Card('d', '7', 7)
        self.d8 = Card('d', '8', 8)
        self.d9 = Card('d', '9', 9)
        self.dt = Card('d', 'T', 10)
        self.dj = Card('d', 'J', 10)
        self.dq = Card('d', 'Q', 10)
        self.dk = Card('d', 'K', 10)
        self.da = Card('d', 'A', 11)
        self.h2 = Card('h', '2', 2)
        self.h3 = Card('h', '3', 3)
        self.h4 = Card('h', '4', 4)
        self.h5 = Card('h', '5', 5)
        self.h6 = Card('h', '6', 6)
        self.h7 = Card('h', '7', 7)
        self.h8 = Card('h', '8', 8)
        self.h9 = Card('h', '9', 9)
        self.ht = Card('h', 'T', 10)
        self.hj = Card('h', 'J', 10)
        self.hq = Card('h', 'Q', 10)
        self.hk = Card('h', 'K', 10)
        self.ha = Card('h', 'A', 11)
        self.s2 = Card('s', '2', 2)
        self.s3 = Card('s', '3', 3)
        self.s4 = Card('s', '4', 4)
        self.s5 = Card('s', '5', 5)
        self.s6 = Card('s', '6', 6)
        self.s7 = Card('s', '7', 7)
        self.s8 = Card('s', '8', 8)
        self.s9 = Card('s', '9', 9)
        self.st = Card('s', 'T', 10)
        self.sj = Card('s', 'J', 10)
        self.sq = Card('s', 'Q', 10)
        self.sk = Card('s', 'K', 10)
        self.sa = Card('s', 'A', 11)
        # a deck (list) of card classes
        self.full_deck  = [self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.ct,self.cj,self.cq,self.ck,self.ca]
        self.full_deck += [self.d2,self.d3,self.d4,self.d5,self.d6,self.d7,self.d8,self.d9,self.dt,self.dj,self.dq,self.dk,self.da]
        self.full_deck += [self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.ht,self.hj,self.hq,self.hk,self.ha]
        self.full_deck += [self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.st,self.sj,self.sq,self.sk,self.sa]

    def __str__(self) -> str:
        the_str = ''
        for card in self.full_deck:
            the_str = the_str + card.shorthand + ' '
        return the_str

class Card():
    def __init__(self, suit, rank, simple_strength_value) -> None:
        self.suit = suit
        self.rank = rank
        self.simple_strength_value = simple_strength_value
        self.shorthand = f'{self.suit}{self.rank}'

    def __str__(self) -> str:
        return self.shorthand

class Hand():
    def __init__(self, owner, card1, card2) -> None:
        self.owner = owner
        self.the_cards = [card1, card2]
        self.score = 0
        self.aces_counter = 0
        for c in self.the_cards:
            self.score+= c.simple_strength_value

    def __str__(self):
        str1 = (f'{self.owner}: ')
        str2=''
        for c in self.the_cards:
            str2 += str(c) 
            str2 += ' '
        str3 = str(self.score)
        str4 = str1 + str2 + '(' + str(self.score) + ')'
        return str4

    def twist(self, new_card):
        self.the_cards.append(new_card)
        # handle aces
        if new_card.rank == 'A':
            self.aces_counter += 1
        self.score += new_card.simple_strength_value
    
    def adjust_score_for_aces(self):
        while self.score > 21 and self.aces_counter > 0:
            self.score -= 10
            self.aces_counter -= 1

class Money():
    def __init__(self, amount) -> None:
        self.amount = amount
    
    def __str__(self):
        return (f'${self.amount}')
    
    def decrease_amount(self, val):
        self.amount -= val    
        print(f'player has ${self.amount}')

    def increase_amount(self, val):
        self.amount += val
        print(f'player has ${self.amount}')


def human_play_blackjack(hand, deck):
    print(hand)

    if hand.score >= 21:
        return hand.score

    # human gameplay loop
    while True:
        # checking user input loop
        while True:
            try: # possibly an exception from this block
                stick_or_twist = input("stick 's' or twist 't'? ")
                if stick_or_twist.lower() == 's' or stick_or_twist.lower() == 't': 
                    break
            except Exception as e: # handle exception if thrown
                print(e)
                continue
            else: # if no exception thrown, exceute this block
                print("input either 's' to stick or 't' to twist")
                continue

        if stick_or_twist == 's':
            return hand.score
        else:
            hand.twist(deck.full_deck.pop())
            hand.adjust_score_for_aces()
            print(hand)
            if hand.score >= 21:
                return hand.score

def dealer_play_blackjack(hand, deck):
    # dealer gameplay loop
    while True:
        print(hand)
        if hand.score >= 17:
            return hand.score
        hand.twist(deck.full_deck.pop())
        hand.adjust_score_for_aces()

def check_for_immediate_blackjack(hand):
    if hand.score == 21:
        return True


if __name__ == '__main__':
    # player's money
    player_money = Money(10)
    print(f'player has {player_money.amount}')
    bet_per_game = 2

    # keep playing games of blackjack loop
    play_again_loop = True
    while play_again_loop == True:
        # get a deck of cards and shuffle it
        deck = Deck()
        random.shuffle(deck.full_deck)
        # deal the first two cards to player and the dealer (hide one of the dealer's cards)
        card_one = deck.full_deck.pop()
        card_two = deck.full_deck.pop()
        card_three = deck.full_deck.pop()
        card_four = deck.full_deck.pop()

        card_one = Card('c','10',10)
        card_two = Card('d','10',10)
        card_three = Card('h','A',10)
        card_four = Card('s','A',10)

        player_hand = Hand('player', card_one, card_three)
        dealer_hand = Hand('dealer', card_two, card_four)
        # show one of the dealer's cards
        print(f"dealer's hand: {dealer_hand.the_cards[0].shorthand} XX")

        player_immediate_21 = check_for_immediate_blackjack(player_hand)
        dealer_immediate_21 = check_for_immediate_blackjack(dealer_hand)
        if player_immediate_21 == True:
            if dealer_immediate_21 == True:
                print('player and dealer both get immediate blackjack - draw')
            else:
                print('player gets blackjack - player wins double!')
                player_money.increase_amount(bet_per_game*2)
            continue

        human_score = human_play_blackjack(player_hand, deck)
        print(f'--{player_hand.owner} score is: {player_hand.score}')
        if (human_score) > 21:
            print('player bust - dealer wins!')
            player_money.decrease_amount(bet_per_game)
        else:
            dealer_score = dealer_play_blackjack(dealer_hand, deck)
            print(f'--{dealer_hand.owner} score is: {dealer_hand.score}')
            if dealer_score > 21:
                print('dealer bust - player wins!')
                player_money.increase_amount(bet_per_game)

        if human_score <= 21 and dealer_score <= 21:
            print(f'player has {player_hand.score}, dealer has {dealer_hand.score}')
            if (human_score > dealer_score):
                print('player wins!')
                player_money.increase_amount(bet_per_game)
            else:
                print('dealer wins!')
                player_money.decrease_amount(bet_per_game)

        if player_money.amount < bet_per_game:
            print("player doesn't have enough money to play - the casino always wins - bye!")
            break
        print('')
        # checking user input loop to see if they want to continue playing
        while True:
            try: # possibly an exception from this block
                again = input('want to play again? y or n: ')
                if again.lower() == 'y' or again.lower() == 'n':
                    break
            except Exception as e: # handle exception if thrown 
                print(e) 
                continue
            else: # if no exception thrown, exceute this block
                print('please input y or n') 
                continue

        if again == 'n':
            play_again_loop = False


