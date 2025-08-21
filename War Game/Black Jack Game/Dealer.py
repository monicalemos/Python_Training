class Dealer:
    def __init__(self):
        self.hand = []

    def stand(self):
        pass

    def hit(self, card):
        self.add_cards(card)

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

if __name__ == "__main__":
    pass