"""
Deck class will contain a list of cards
"""
import random
from Card import Card
from SuitEnum import SuitEnum
from RankEnum import RankEnum

class Deck:
    #@property
    #def max_size(self):
    #    return 52
    max_size = 52

    def __init__(self, cards=None):
        if cards is None or len(cards) == 0:
            self.cards = []

            for suit in SuitEnum:
                for rank in RankEnum:
                    card = Card(suit, rank)
                    self.cards.append(card)
        elif len(cards) < self.max_size :
            raise ValueError("The Deck must have 52 cards")
        elif len(cards) > self.max_size :
            raise ValueError("The Deck must have 52 cards")
        else:
            if type(cards) is not list and type(cards[0]) is not Card:
                raise TypeError(f'Invalid type for Cards')
            self.cards = cards

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop(0)

if __name__ == "__main__":
    pass

