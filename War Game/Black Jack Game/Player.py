"""
Player will have a name and a hand of cards
"""
from Deck import Deck
from GameException import GameException

class Player:

    def __init__(self, name, start_amount):
        self.name = name
        self.hand = []
        self.bank_roll = start_amount

    def stand(self):
        pass

    def hit(self, card):
        self.add_cards(card)

    def bet(self, amount):
        if self.bank_roll >= amount:
            self.bank_roll -= amount
        else:
            raise GameException(f"The player don't have enough money to bet that amount! Current balance is {self.bank_roll}")

    def sum_hand(self):
        sum_cards = 0
        for card in self.hand:
            sum_cards += card.value
        return sum_cards

    def add_cards(self, new_cards):
        if type(new_cards) is list:
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def num_cards(self):
        return len(self.hand)

    def wins(self, amount):
        self.bank_roll += amount

    def __str__(self):
        return f'Player {self.name} has {len(self.bank_roll)} cards in hand and {self.bank_roll} in account'

if __name__ == "__main__":
    pass