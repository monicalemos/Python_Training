"""
Player will have a name and a hand of cards
"""
from Deck import Deck
from GameException import GameException

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_one(self):
        return self.hand.pop(0)

    def play_cards(self, num_cards):
        if self.num_cards() > num_cards :
            pile = []
            for i in range(num_cards):
                pile.append(self.play_one())
            return pile
        else:
            raise GameException(f"{self.name} doesn't have enough cards to play")

    def add_cards(self, new_cards):
        if type(new_cards) is list:
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def num_cards(self):
        return len(self.hand)

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards in hand'

if __name__ == "__main__":
    pass