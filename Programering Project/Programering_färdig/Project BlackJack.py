import random



class Interaction():
    def UserInputHandeler(self, question) -> int:
        bad_user_input: bool = True
        while bad_user_input:
            user_input: int = input(question).lower()
            if user_input.isdigit():
                user_input = int(user_input)
                bad_user_input = False
        return user_input
    
    def YesNoHandler(self, question) -> bool:
        while True:
            user_input: str = input(question).lower()
            if user_input in ['yes', 'y', 'ye', 'yea', 'ja']:
                print("\n")
                return True
            elif user_input in ['no', 'n', 'nej']:
                print("Thanks for playing :)")
                return False
            else:
                print("Please enter 'yes' or 'no'.")


class BettingGame:
    def __init__(self) -> None:
        self.worth: float = 100.0
        self.current_bet: int = 0
        self.user_input: Interaction = Interaction()

    def placeBet(self) -> int:
        while True:
            self.current_bet = self.user_input.UserInputHandeler(f"How much do you want to bet? You currently have: {self.worth}\nHow much do you dare to bet: (enter number between 1 and {self.worth}): ")
            if self.current_bet > self.worth:
                print("You cannot bet more than what you have.")
            else:
                break
        self.worth -= self.current_bet  

class Card:
    def __init__(self, value, name) -> None:
        self.value: int = value
        self.name: str = name

class Deck:
    def __init__(self) -> None:
        self.deck = [
            Card(2, "of Hearts"), Card(3, "of Hearts"), Card(4, "of Hearts"), Card(5, "of Hearts"),
            Card(6, "of Hearts"), Card(7, "of Hearts"), Card(8, "of Hearts"), Card(9, "of Hearts"),
            Card(10, "of Hearts"), Card(2, "of Diamonds"), Card(3, "of Diamonds"), Card(4, "of Diamonds"),
            Card(5, "of Diamonds"), Card(6, "of Diamonds"), Card(7, "of Diamonds"), Card(8, "of Diamonds"),
            Card(9, "of Diamonds"), Card(10, "of Diamonds"), Card(2, "of Clubs"), Card(3, "of Clubs"),
            Card(4, "of Clubs"), Card(5, "of Clubs"), Card(6, "of Clubs"), Card(7, "of Clubs"),
            Card(8, "of Clubs"), Card(9, "of Clubs"), Card(10, "of Clubs"), Card(2, "of Spades"),
            Card(3, "of Spades"), Card(4, "of Spades"), Card(5, "of Spades"), Card(6, "of Spades"),
            Card(7, "of Spades"), Card(8, "of Spades"), Card(9, "of Spades"), Card(10, "of Spades"),
            Card(10, "Jack of Hearts"), Card(10, "Queen of Hearts"), Card(10, "King of Hearts"),
            Card(11, "Ace of Hearts"), Card(10, "Jack of Diamonds"), Card(10, "Queen of Diamonds"),
            Card(10, "King of Diamonds"), Card(11, "Ace of Diamonds"), Card(10, "Jack of Clubs"),
            Card(10, "Queen of Clubs"), Card(10, "King of Clubs"), Card(11, "Ace of Clubs"),
            Card(10, "Jack of Spades"), Card(10, "Queen of Spades"), Card(10, "King of Spades"),
            Card(11, "Ace of Spades")
        ]

    def DrawCard(self) -> Card:
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

class Hand:
    def __init__(self, name) -> None:
        self.name = name
        self.hand: list[str] = []
        self.turn: list[int] = []
        self.total_value: int = 0

    def dealCard(self, card) -> None:
        self.turn.append(card)
        
    def calculate_total(self) -> None:
        self.total_value = 0
        for card in self.turn:
            if card.value <= 10:
                self.total_value += card.value
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
    def __init__(self, betting: BettingGame) -> None:
        self.player_in = True
        self.dealer_in = True
        self.stayOrHit: int = 0
        self.player = Hand("Player")
        self.dealer = Hand("Dealer")
        self.deck = Deck()
        self.betting = betting
        self.user_input = Interaction()

    
    def PrintPlayerHand(self):
        for i in range(len(self.player.turn)):
            print("",self.player.turn[i].name, self.player.turn[i].value, end='')
    
    def PrintDealerHand(self):
        for i in range(len(self.dealer.turn)):
            print("", self.dealer.turn[i].name, self.dealer.turn[i].value, end='')

    def game(self) -> None:
        for i in range(2):
            self.player.dealCard(self.deck.DrawCard())
            self.dealer.dealCard(self.deck.DrawCard())
        self.player.calculate_total()
        self.dealer.calculate_total()
        self.betting.placeBet()

        while self.player_in or self.dealer_in:
            if self.player_in:
                print(f"Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and x")
                print("You have", end='')
                self.PrintPlayerHand()
                print(" for a total of:", self.player.total_value)
                if self.player.total_value == 21:
                    self.stayOrHit = 1
                else:
                    self.stayOrHit = self.user_input.UserInputHandeler("1: Stay\n2: Hit\n")
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
            print("Blackjack! You win! Your hand:", end='')
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            self.betting.worth += self.betting.current_bet * 2
            print(f"You are now worth: {self.betting.worth}")
        elif self.dealer.total_value == 21:
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            print(f"You are now worth: {self.betting.worth}")
        elif self.player.total_value > 21:
            print(f"You bust! Dealer wins! Your hand:", end='')
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            print(f"You are now worth: {self.betting.worth}")
        elif self.dealer.total_value > 21:
            print("Dealer busts! You win! Your hand:", end='')
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            self.betting.worth += self.betting.current_bet * 1.5
            print(f"You are now worth: {self.betting.worth}")
        elif self.player.total_value > self.dealer.total_value:
            print("You win! Your hand:", end='')
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            self.betting.worth += self.betting.current_bet * 1.5
            print(f"You are now worth: {self.betting.worth}")
        else:
            print("Dealer wins! Your hand:",end='')
            self.PrintPlayerHand()
            print(" for a total of:", self.player.total_value)
            print("Dealer hand:", end='')
            self.PrintDealerHand()
            print(" for a total of:", self.dealer.total_value)
            print(f"You are now worth: {self.betting.worth}")

def main():
    interaction = Interaction()
    play_again = True
    betting_game = BettingGame()
    while play_again:
        if betting_game.worth <= 0.0:
            print("You can't play again because you are broke and cannot bet anymore")
            print("To play again you can either rerun the code or make some mone somewere else (like getting a job :) ")
            break
        spela = Play(betting_game)
        spela.game()
        play_again = interaction.YesNoHandler("Do you want to play again? (yes/no): ")


if __name__ == "__main__":
    main()