"""
Game will have 2 players
"""
from Deck import Deck
from Player import Player

from datetime import date
from WarGameException import GameException

class Game:
    def __init__(self, date, player1, player2):
        self.date = date
        self.deck = Deck()

        self.player1 = player1
        self.player2 = player2

    def play_game(self, num_cards_in_play):

        #distribute cards
        self.deck.shuffle()

        player1_hand = []
        player2_hand = []
        for i in range(int(num_cards_in_play/2)):
            player1_hand.append(self.deck.deal_one())
            player2_hand.append(self.deck.deal_one())

        self.player1.add_cards(player1_hand)
        self.player2.add_cards(player2_hand)
        print(f'Player 1 will be {self.player1.name}  - hand: {self.player1.hand}')
        print(f'Player 2 will be {self.player2.name}  - hand: {self.player2.hand}')
        print()

        # Check at beginning
        game_ended = self.player1.num_cards() == 0 or self.player2.num_cards() == 0

        count_rounds = 1
        while not game_ended:
            print("\n-------------------------------------------------------")
            print("----- LETS PLAY")
            try :
                cards_lost_player1 = self.player1.num_cards()
                cards_lost_player2 = self.player2.num_cards()
                play_result = self.play()
                card_for_player1 = play_result[0]
                card_for_player2 = play_result[1]

                self.player1.add_cards(card_for_player1)
                self.player2.add_cards(card_for_player2)

                cards_lost_player1 -= self.player1.num_cards()
                cards_lost_player2 -= self.player2.num_cards()

                #check status
                game_ended = self.player1.num_cards() == 0 or self.player2.num_cards() == 0
                print(f'\nResults after round {count_rounds}')
                print(f'\t---> {self.player1}, wins {len(card_for_player1)} cards and lost {cards_lost_player1} cards.')
                print(f'\t---> {self.player2}, wins {len(card_for_player2)} cards and lost {cards_lost_player2} cards.')
                print(f'\t---> Game has ended? {game_ended}')
                count_rounds += 1
            except GameException as e:
                print(f'---> Game has ended. {e.message}')
                game_ended = True
            print("\n-------------------------------------------------------")

        #Get final results!
        player1_hand_size = self.player1.num_cards()
        player2_hand_size = self.player2.num_cards()
        if player1_hand_size > player2_hand_size:
            print(f'\n{self.player1.name} wins in {count_rounds} rounds! At the end of the game the status is {str(len(self.player1.hand))} vs {str(len(self.player2.hand))}.')
        else:
            print(f'\n{self.player2.name} wins in {count_rounds} rounds! At the end of the game the status is {str(len(self.player2.hand))} vs {str(len(self.player1.hand))}')

    def play(self):
        player1_cards = []
        player2_cards = []

        card_for_player1 = []
        card_for_player2 = []

        war_is_on = True
        count_war = 0

        while war_is_on :
            if self.player1.num_cards() == 0 or self.player2.num_cards() == 0:
                #The players can't continue the game
                break

            card_player1 = self.player1.play_one()
            player1_cards.append(card_player1)  # Add card from player 1
            print(f'---> {self.player1.name} have played card: {card_player1}')

            card_player2 = self.player2.play_one()
            player2_cards.append(card_player2)  # Add self card
            print(f'---> {self.player2.name} have played card: {card_player2}')

            if card_player1 > card_player2:
                # Player 1 wins
                war_is_on = False

                card_for_player1.extend(player1_cards)  # Add all the cards drawn from himself
                card_for_player1.extend(player2_cards)  # Add all the cards drawn from player 1
                print(f'\t---> {card_player1} > {card_player2} ({card_player1.value} > {card_player2.value})')

            elif card_player2 > card_player1:
                # Player 2 wins
                war_is_on = False

                card_for_player2.extend(player1_cards) # Add all the cards drawn from player 1
                card_for_player2.extend(player2_cards) # Add all the cards drawn from himself
                print(f'\t---> {card_player2} > {card_player1} ({card_player2.value} > {card_player1.value})')

            elif card_player1 == card_player2:  # War scenario
                print_str = '\t---> Woops is WAR Time!!'
                if count_war > 0:
                    print_str += f'---- The war continues for the {count_war > 0} time!!'
                print_str += f'{card_player1} with value {card_player1.value} IS EQUAL TO {card_player2} with value {card_player2.value}'
                print(print_str)
                player1_cards.extend(self.player1.play_cards(5))
                player2_cards.extend(self.player2.play_cards(5))


        return [card_for_player1, card_for_player2]



if __name__ == "__main__":
    pl1 = Player(name="Jose")
    pl2 = Player(name="Maria")
    game = Game(date.today(), pl2, pl1)

    num_cards = int(len(game.deck))
    #num_cards = 16
    game.play_game(num_cards)