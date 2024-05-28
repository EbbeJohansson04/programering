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

class BettingGame:
    def __init__(self) -> None:
        self.worth: float = 100.0
        self.current_bet: int = 0
        self.user_input: Interaction = Interaction()

    def placeBet(self) -> int:
        self.current_bet: int = self.user_input.UserInputHandeler(f"How much do you want to bet? You currently have: {self.worth}\nHow much do you dare to bet: (enter number between 1 and {self.worth}): ")
        self.worth -= self.current_bet  

class Card:
    def __init__(self, name, value) -> None:
        self.name: str = name
        self.value: int = value

class Deck:
    def __init__(self) -> None:
        self.deck = [Card("Hearts", 2), Card("Hearts",3), Card("Hearts",4), Card("Hearts",5), Card("Hearts",6), Card("Hearts",7), Card("Hearts",8), Card("Hearts",9), Card("Hearts",10), Card("Diamonds",2), Card("Diamonds",3), Card("Diamonds",4), Card("Diamonds",5), Card("Diamonds",6), Card("Diamonds",7), Card("Diamonds",8), Card("Diamonds",9), Card("Diamonds",10), Card("Clubs",2), Card("Clubs",3), Card("Clubs",4), Card("Clubs",5), Card("Clubs",6), Card("Clubs",7), Card("Clubs",8), Card("Clubs",9), Card("Clubs",10),
                     Card("Spades",2), Card("Spades",3), Card("Spades",4), Card("Spades",5), Card("Spades",6), Card("Spades",7), Card("Spades",8), Card("Spades",9), Card("Spades",10), Card("Hearts Jack",10), Card("Hearts Queen",10), Card("Hearts King",10), Card("Hearts Ace",11), Card("Diamonds Jack",10), Card("Diamonds Queen",10), Card("Diamonds King",10), Card("Diamonds Ace",11), Card("Clubs Jack",10), Card("Clubs Queen",10), Card("Clubs King",10), Card("Clubs Ace",11), Card("Spades Jack",10), Card("Spades Queen",10), Card("Spades King",10), Card("Spades Ace",11)]

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
    def __init__(self) -> None:
        self.player_in = True
        self.dealer_in = True
        self.stayOrHit: int = 0
        self.player = Hand("Player")
        self.dealer = Hand("Dealer")
        self.deck = Deck()
        self.betting = BettingGame()
        self.user_input = Interaction()
    
    def PrintPlayerHand(self):
        for i in range(len(self.player.turn)):
            print(" ",self.player.turn[i].name, self.player.turn[i].value, end='')

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
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth += self.betting.current_bet * 2
            print(f"You are now worth: {self.betting.worth}")
        elif self.dealer.total_value == 21:
            print("Blackjack! Dealer wins! Your hand:", end='')
            self.PrintPlayerHand()
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth -= self.betting.current_bet
            print(f"You are now worth: {self.betting.worth}")
        elif self.player.total_value > 21:
            print(f"You bust! Dealer wins! Your hand:", end='')
            self.PrintPlayerHand()
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth -= self.betting.current_bet
            print(f"You are now worth: {self.betting.worth}")


        elif self.dealer.total_value > 21:
            print("Dealer busts! You win! Your hand:", end='')
            self.PrintPlayerHand()
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth += self.betting.current_bet * 1.5
            print(f"You are now worth: {self.betting.worth}")



        elif self.player.total_value > self.dealer.total_value:
            print("You win! Your hand:", end='')
            self.PrintPlayerHand()
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth += self.betting.current_bet * 1.5
            print(f"You are now worth: {self.betting.worth}")
        else:
            print("Dealer wins! Your hand:",end='')
            self.PrintPlayerHand()
            print(f" Dealer has {self.dealer.turn[0].name} {self.dealer.turn[0].value} and {self.dealer.turn[1].name} {self.dealer.turn[1].value}")
            self.betting.worth -= self.betting.current_bet
            print(f"You are now worth: {self.betting.worth}")

spela = Play()
spela.game()
