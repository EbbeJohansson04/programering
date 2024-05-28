import random

class Beting:
    def __init__(self) -> None:
        self.worth: int = 100
        self.betting: int = int(input(f"You currently have: {self.worth}\nHow much do you dare to bet: (enter number between 1 and {self.worth}) "))


class Deck:
    def __init__(self) -> None:
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]

class Hand:
    def __init__(self, name) -> None:
        self.name = name
        self.hand: list[str] = []
        self.turn: list[int] = []
        self.total_value: int = 0
        self.FACE: list[str] = ["J", "Q", "K"]
        self.deck = Deck()
        
    def dealCard(self):
        for _ in range(2):
            card = random.choice(self.deck.deck)
            self.turn.append(card)
            self.deck.deck.remove(card)
        
    def calculate_total(self) -> None:
        self.total_value = 0
        for card in self.turn:
            if isinstance(card, int):
                self.total_value += card
            elif card in self.FACE:
                self.total_value += 10
            else:  # Ace handling
                if self.total_value > 10:
                    self.total_value += 1
                else:
                    self.total_value += 11

class Dealer:
    def __init__(self) -> None:
        self.hand = []
        self.turn: list[int] = []
        self.total_value: int = 0

    def revealDealerHand(self):
        if len(self.turn) == 2:
            return self.turn[0]
        elif len(self.turn) > 2:
            return self.turn[1]

class Play:
    def __init__(self) -> None:
        self.player_in = True
        self.dealer_in = True
        self.stayOrHit: int = 0
        self.player = Hand("Player")
        self.dealer = Hand("Dealer")
        self.deck = Deck()

    def game(self) -> None:
        self.player.dealCard()
        self.dealer.dealCard()
        self.player.calculate_total()
        self.dealer.calculate_total()
        self.beting: int = int(input(f"You currently have: {self.worth}\nHow much do you dare to bet: (enter number between 1 and {self.worth}) "))

        while self.player_in or self.dealer_in:
            print(f"Dealer has {self.dealer.turn[0]} and x")
            print(f"You have {self.player.turn} for a total of {self.player.total_value}")
            if self.player_in:
                self.stayOrHit = int(input("1: Stay\n2: Hit\n"))
                if self.stayOrHit == 1:
                    self.player_in = False
                elif self.stayOrHit == 2:
                    card = random.choice(self.deck.deck)
                    self.player.turn.append(card)
                    self.deck.deck.remove(card)
                    self.player.calculate_total()
                    if self.player.total_value >= 21:
                        self.player_in = False

            if self.dealer.total_value > 16:
                self.dealer_in = False
            else:
                card = random.choice(self.deck.deck)
                self.dealer.turn.append(card)
                self.deck.deck.remove(card)
                self.dealer.calculate_total()
                if self.dealer.total_value >= 21:
                    self.dealer_in = False

        self.determine_winner()

    def determine_winner(self):
        if self.player.total_value == 21:
            print(f"Blackjack! You win! Your hand: {self.player.turn},for a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth += self.beting * 2
        elif self.dealer.total_value == 21:
            print(f"Blackjack! Dealer wins! Your hand: {self.player.turn}, for a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth -= self.beting
        elif self.player.total_value > 21:
            print(f"You bust! Dealer wins! Your hand: {self.player.turn}, for a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth -= self.beting
        elif self.dealer.total_value > 21:
            print(f"Dealer busts! You win! Your hand: {self.player.turn}, for a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth += self.beting * 1.5
        elif self.player.total_value > self.dealer.total_value:
            print(f"You win! Your hand: {self.player.turn}, Dfor a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth += self.beting * 1.5
        else:
            print(f"It is a tie so Dealer wins! Your hand: {self.player.turn}, for a total of: {self.player.total_value} \nDealer's hand: {self.dealer.turn} for a total of {self.dealer.total_value}")
            self.worth -= self.beting

spela = Play()
spela.game()
