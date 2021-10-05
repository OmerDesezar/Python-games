# -----------------------------------------------------------------------------------------------------------------------
# war

import random

# Constants
suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# Classes
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.card_deck = []
        for rank in ranks:
            for suit in suits:
                self.card_deck.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.card_deck)

    def deal_card(self):
        return self.card_deck.pop()

    def print_deck(self):
        for card in self.card_deck:
            print(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.p_deck = []

    def __str__(self):
        return f'Player {self.name} has {len(self.p_deck)} cards'

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.p_deck.extend(cards)
        else:
            self.p_deck.append(cards)

    def bet_card(self):
        return self.p_deck.pop(0)

    def shuffle_p_deck(self):
        random.shuffle(self.p_deck)


# Functions
def either_deck_empty():
    if len(player1.p_deck) == 0 or len(player2.p_deck) == 0:
        return True


def game_over():
    if len(player1.p_deck) == 0:
        print(f'Player 2, {player2.name}, won the game after {round_num-1} rounds!')
    elif len(player2.p_deck) == 0:
        print(f'Player 1, {player1.name}, won the game after {round_num-1} rounds!')
    else:
        print('Tie')


def new_war():
    current_war = [player1.bet_card(), player2.bet_card()]
    print(f'Player 1 drew {current_war[0]}')
    print(f'Player 2 drew {current_war[1]}')

    while current_war[-1].value == current_war[-2].value:
        if either_deck_empty():
            break
        print('A war!')

        for i in range(4):
            current_war.append(player1.bet_card())
            current_war.append(player2.bet_card())
            if either_deck_empty():
                break

        print(f'After betting {len(current_war) / 2} cards each..')
        print(f'Player 1 drew {current_war[-2]}')
        print(f'Player 2 drew {current_war[-1]}')

    p1_last_card = current_war[-2]
    p2_last_card = current_war[-1]
    half_prize_pile = len(current_war) // 2

    if p1_last_card.value > p2_last_card.value:
        print(f'Player 1 got {half_prize_pile} cards for winning round {round_num}')
        player1.add_cards(current_war)
    elif p1_last_card.value < p2_last_card.value:
        print(f'Player 2 got {half_prize_pile} cards for winning round {round_num}')
        player2.add_cards(current_war)
    else:
        if len(player1.p_deck) == 0:
            print(f'Player 2 got {half_prize_pile} cards for winning round {round_num}')
            player2.add_cards(current_war)
        elif len(player2.p_deck) == 0:
            print(f'Player 1 got {half_prize_pile} cards for winning round {round_num}')
            player1.add_cards(current_war)
        else:
            print('Round tie, dividing evenly')
            player1.add_cards(current_war[::half_prize_pile])
            player1.add_cards(current_war[half_prize_pile::])


# Game
player1 = Player(input("Player 1 enter your name: "))
player2 = Player(input("Player 2 enter your name: "))

full_deck = Deck()
full_deck.shuffle_deck()
for _ in range(len(full_deck.card_deck) // 2):  # splitting deck to both players
    player1.add_cards(full_deck.deal_card())
    player2.add_cards(full_deck.deal_card())

game_running = True
round_num = 0

while game_running:
    round_num += 1
    print('---------------------------------------------------')
    print(f'Round {round_num}')
    print(player1)
    print(player2)
    print('---------------------------------------------------')
    if either_deck_empty():
        game_running = False
        break
    player1.shuffle_p_deck()
    player2.shuffle_p_deck()
    new_war()

game_over()

# -----------------------------------------------------------------------------------------------------------------------
