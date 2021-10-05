# -----------------------------------------------------------------------------------------------------------------------
# blackjack

import random

# Constants
suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# Classes
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit} ({self.value})'


class Deck:
    def __init__(self):
        self.card_deck = []
        for rank in ranks:
            for suit in suits:
                self.card_deck.append(Card(rank, suit))
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.card_deck)

    def deal_card(self):
        return self.card_deck.pop()

    def print_deck(self):
        for card in self.card_deck:
            print(card)


class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
        self.p_deck = []

    def __str__(self):
        return f'Your current hands sum is {self.sum_cards()}.'

    def add_card(self, card):
        self.p_deck.append(card)

    def show_bankroll(self):
        return f'You have {self.bankroll} dollars left.'

    def bet_money(self, num):
        if self.bankroll >= num:
            self.bankroll -= num
            return True
        else:
            print('Not enough funds')
            return False

    def win_money(self, num):
        self.bankroll += num*2

    def sum_cards(self):
        card_sum = 0
        contains_ace = False

        for card in self.p_deck:
            card_sum += card.value
            if card.rank == 'Ace':
                contains_ace = True

        if card_sum > 21 and contains_ace:
            card_sum -= 10
        return card_sum

    def last_card(self):
        return self.p_deck[-1]


# Functions
def deal_first_cards():
    dealer.add_card(game_deck.deal_card())
    player1.add_card(game_deck.deal_card())
    dealer.add_card(game_deck.deal_card())
    player1.add_card(game_deck.deal_card())
    print(f'The dealer open card is a {dealer.p_deck[0]}')
    print(f'Your cards are a {player1.p_deck[0]} and a {player1.p_deck[1]}')

def reset_round():
    global winner
    game_deck.__init__()
    winner = None
    player1.p_deck = []
    dealer.p_deck = []

def is_bust(player):
    if player.sum_cards() > 21:
        return True
    return False

def check_game_over():
    if type(winner) != type(None):
        if winner:
            print(f'{player1.name} wagered {current_prize_pool} dollars and won!')
            player1.win_money(current_prize_pool)
        else:
            print(f'{player1.name} wagered {current_prize_pool} dollars and lost')
        return True
    return False


# Game
game_deck = Deck()

p1_name = input("Enter your name: ")
while True:
    try:
        p1_money = int(input("How much money you got? "))
    except:
        print("That wasn't a number, please try again.")
    else:
        break

player1 = Player(p1_name, p1_money)
dealer = Player("Dealer", 0)
winner = None

still_playing = True
while still_playing:
    if player1.bankroll == 0 or input("Do you want to continue? ('no' to quit, anything else to continue)") == 'no':
        print('Game over!')
        still_playing = False
        break
    print('-----------------------------------------------------------------')

    # Choose wager money
    current_prize_pool = 0
    while current_prize_pool == 0:
        print(player1.show_bankroll())
        while True:
            try:
                to_bet = int(input("how much you want to wager this round? "))
            except:
                print("That wasn't a number, please try again.")
            else:
                break

        if player1.bet_money(to_bet):
            current_prize_pool = to_bet
            print(f'current prize pool: {current_prize_pool}')
            print(player1.show_bankroll())
            
    reset_round()
    deal_first_cards()

    # Player turn
    while True:
        print(player1)
        if is_bust(player1):
            print('Bust')
            winner = False
            break
        action = input('Would you like to hit or stay? ')
        if action == 'hit':
            player1.add_card(game_deck.deal_card())
            print(f'You opened a {player1.last_card()}')
        elif action == 'stay':
            break
        else:
            print('not a valid action')

    if check_game_over():
        continue

    # Dealer turn
    print(f'Dealers second card was a {dealer.p_deck[1]}')
    while dealer.sum_cards() <= player1.sum_cards() and not is_bust(dealer):
        print(f'Dealers current sum is {dealer.sum_cards()}')
        dealer.add_card(game_deck.deal_card())
        print(f'Dealer opened a {dealer.last_card()}')
    print(f'Dealer final sum is {dealer.sum_cards()}')
    print(f'Your final sum is {player1.sum_cards()}')
    if is_bust(dealer):
        winner = True
    else:
        winner = False
    check_game_over()

# -----------------------------------------------------------------------------------------------------------------------
