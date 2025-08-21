"""
Class created to represent a Card
SUIT - diamonds, clubs, hearts, spades - use enum Suit to pass the value
RANK
VALUE
"""

from SuitEnum import SuitEnum
from RankEnum import RankEnum

class Card:

    def __init__(self, suit, rank):
        if type(suit) == SuitEnum:
            self.suit = suit
        elif type(suit) == RankEnum:
            self.rank = suit
        else:
            raise TypeError(f'Invalid type for Suit')

        if type(rank) == SuitEnum:
            self.suit = rank
        elif type(rank) == RankEnum:
            self.rank = rank
        else:
            raise TypeError(f'Invalid type for Rank')

        self.value = self.rank.value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __eq__(self, other):
        return self.rank.value == other.rank.value

    def __lt__(self, other):
        return self.rank.value < other.rank.value

    def __le__(self, other):
        return self.rank.value <= other.rank.value

    def __gt__(self, other):
        return self.rank.value > other.rank.value

    def __ge__(self, other):
        return self.rank.value >= other.rank.value

if __name__ == "__main__":
    pass

