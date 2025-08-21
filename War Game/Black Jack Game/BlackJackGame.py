from openpyxl.pivot.fields import Boolean

from Deck import *
from Player import *
from Dealer import *
from GameException import *

def hit_or_stand():
    hit_choice = ""
    while not hit_choice not in ["Y", "N"]:
        hit_choice = input("Would you like to hit another card? (Y/N): ")
    return hit_choice == "Y"

def is_bust(hand):
    sum_cards = 0
    for card in hand:
        sum_cards += card.value

    return sum_cards > 21

def is_blackjack(hand):
    sum_cards = 0
    for card in hand:
        sum_cards += card.value

    return sum_cards == 21

class BlackJackGame:

    def __init__(self, deck, player):
        self.deck = deck
        self.player = player
        self.dealer = Dealer()


    def play(self):


        keep_playing = True
        player_lost = False

        while keep_playing:
            bet_amount = self.bet()
            self.start_game()

            is_under_21 = True
            while is_under_21:

                hit_choice = hit_or_stand()

                if hit_choice  :
                    new_card = self.deck.deal_one()
                    print(f"The player got card {new_card}")
                    self.player.hit(new_card)
                    is_under_21 = not is_bust(self.player.hand)
                    if is_under_21:
                        player_lost = True

                else:  # stand
                    print("The player choose to stand!")
                    while self.dealer.sum_hand() < 17 or is_under_21:
                        new_card = self.deck.deal_one()
                        print(f"The dealer got card {new_card}")
                        self.dealer.hit(new_card)
                        is_under_21 = not is_bust(self.dealer.hand)
                        if not is_under_21 and not player_lost:
                            player_lost = False

            print(f"Player Cards: {self.player.hand}")
            print(f"Dealer Cards: {self.dealer.hand}")

            player_sum_hand = self.player.sum_hand()
            dealer_sum_hand = self.dealer.sum_hand()

            if not player_lost or player_sum_hand.value > dealer_sum_hand.value:
                print("You won!")
            elif player_lost or dealer_sum_hand.value > player_sum_hand.value:
                print("You lost!")
            else:
                print("It was a tie!")
                self.player.wins(bet_amount)

            keep_play_choice = ""
            while not keep_play_choice not in ["Y", "N"]:
                keep_play_choice = input("Do you want to play again? (Y/N): ")

            keep_playing = keep_play_choice == "y"

    def bet(self):
        valid_bet = False
        bet_amount = 0
        while not valid_bet:
            try:
                bet_amount = float(input("What is your bet?"))
                self.player.bet(bet_amount)
                valid_bet = True
            except GameException as e:
                print(e)
                print("Please provide a new bet!")

        return bet_amount

    def start_game(self):
        dealer_cards = [self.deck.deal_one(), self.deck.deal_one()]
        self.dealer.add_cards(dealer_cards)
        print(dealer_cards[-1])

        player_cards = [self.deck.deal_one(), self.deck.deal_one()]
        self.player.add_cards(player_cards)
        print(player_cards)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    player = Player("João", 100.00)
    game = BlackJackGame(deck, player)
    game.play()
    """
    Logic to be applied:
        01. Create a deck of 52 cards
        02. Shuffle the deck
        03. Ask the Player for their bet
        04. Make sure that the Player's bet does not exceed their available chips
        05. Deal two cards to the Dealer and two cards to the Player
        06. Show only one of the Dealer's cards, the other remains hidden
        07. Show both of the Player's cards
        08. Ask the Player if they wish to Hit, and take another card
        09. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        11. Determine the winner and adjust the Player's chips accordingly
        12. Ask the Player if they'd like to play again
    """
