
import random


#fler spelare#


#player_in = True
#dealer_in = True

#worth = 100

#beting = int(input("How much do dare to bet: "))


class Beting():
    def __init__(self) -> None:
        self.worth = 100
        self.beting = int(input("How much do dare to bet: "))

class Deck():
    def __init__(self)-> None:
#        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                    2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A",  "J", "Q", "K", "A",  "J", "Q", "K", "A", ]
        self.deck = []
        self.create_deck()

    def create_deck(self):
        self.deck = []
        for i in range(1, 14):
            # spade - unicode
            self.cards.append(Card('\u2660', i))
            # heart - unicode
            self.cards.append(Card('\u2665', i))
            # diamond - unicode
            self.cards.append(Card('\u2666', i))
            # club - unicode
            self.cards.append(Card('\u2663', i))





class Card:
    def __init__(self, name, value) -> None:
        self.exist: bool = True
        self.name: str = name
        self.value: value = value
    


class Hand():
    def __init__(self, card, suit, value) -> None:
        self.card: int = card
        self.hand: list[str] = []
        self.turn: list[int] = []
        self.total_value: int = 0
        self.FACE: list[str] = ["J", "Q", "K"]
        self.deck = Deck()
        self.suit = suit
        self.value = value

    def card(self):
        self.card

    def dealCard(self):
        for _ in range(2):
            self.card = random.choice(deck)
            self.turn.append(self.card)
        
    def RemoveValueFromeDeck():
        for i in range(len(self.player.turn)):
            self.deck.deck.remove(self.player.turn[i])
        
    def giveCards(self):
            self.dealCard(self.dealerHand)

    def calculate_total(self) -> None:
        self.total_value = 0
        for card in self.turn:
            if card in range(1, 11):
                self.total_value += card
            elif card in self.face:
                self.total_value += 10
            else:
                if self.total_value > 11:
                    self.total_value += 1
                else:
                    self.total_value += 11

class Dealer():
    def __init__(self) -> None:
        self.hand = []

    def revealDealerHand(self):
        if len(self.dealerHand) == 2:
            return self.dealerHand[0]
        elif len(self.dealerHand) > 2:
            return self.dealerHand[1]


class Play():
    def __init__(self) -> None:
        self.player_in = True
        self.dealer_in = True
        self.stayOrHit = 0
        self.player = Hand("Ada")
        self.computer = Hand("Computer")
        self.deck = Deck()

    def game(self):
        self.player.calculate_total()
        self.player.dealCard()
        

        while self.player_in or self.dealer_in:
            print(F"Dealer has {self.computer.hand} and x")
            print(f"You have {self.player.hand} for a total of {self.player.total}")
        if self.player_in:
            self.stayOrHit = input("1: Stay\n2: Hit\n")
            if self.stayOrHit.isdigit():
                int(self.stayOrHit)
            else:
                print("Please press ether the nr '1' button or nr '2' button and try again")
        if self.total(self.dealerHand) > 16:
            self.dealer_in = False
        else:
            self.dealCard(self.dealerHand)
        if self.stayOrHit == 1:
            self.player_in = False
        else:
            self.dealerCard(self.playerHand)
        if self.total(self.dealrHand) >= 21:
            self.dealer_in = False
        if self.total(self.playerHand) >= 21:
            self.player_in = False

    def sount(self):
        if self.total(self.plaerHand) == 21:
            print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
            print("Black Jack! You win")
            self.worth += self.beting * 2
        elif self.total(self.dealerHand) == 21:
            print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
            print("Black Jack! Dealer wins")
            self.worth -= self.beting
        elif self.total(self.playerHand) > 21:
                print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
                print("You Bust! Dealer wins")
                self.worth -= self.beting
        elif self.total(self.dealerHand) > 21:
                print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
                print("Dealer busts! You win")
                self.worth += self.beting * 1.5
        elif 21 - self.total(self.dealerHand) < 21 - self.total(self.playerHand):
                print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
                print("You win")
                self.worth += self.beting * 1.5
        elif 21 - self.total(self.dealerHand) > 21 - self.total(self.playerHand):
            print(F"\nYou have {self.playerHand} for a total of {self.total(self.playerHand)} an the dealer have {self.dealerHand} for a total of {self.total(self.dealerHand)}")
            print("Dealer Wins")
            self.worth -= self.beting


    def main():
        your_cards = self.dealCards

    def giveCards(self):
        for _ in range(2):
            self.dealCard(self.dealerHand)
            self.dealCard(self.playerHand)

spela = Play()
spela.game()



#deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A",  "J", "Q", "K", "A",  "J", "Q", "K", "A", ]
#playerHand = []
#dealerHand = []

#def dealCard(turn):
#    card = random.choice(deck)
#    turn.append(card)
#    deck.remove(card)

#def total(turn):
#    total = 0
#    face = ["J", "K", "Q"]
#    for card in turn:
#        if card in range(1, 11):
#            total += card
#        elif card in face:
#           total += 10
#        else: 
#            if total > 11:
#                total += 1
#            else: total += 11
#    return total


#def revealDealerHand():
#    if len(dealerHand) == 2:
#        return dealerHand[0]
#    elif len(dealerHand) > 2:
#        return dealerHand[0], dealerHand[1]
    
#for _ in range(2):
#    dealCard(dealerHand)
#    dealCard(playerHand)

#while player_in or dealer_in:
#    print(F"Dealer has {revealDealerHand()} and x")
#    print(f"You have {playerHand}  for a total of {total(playerHand)}")
#    if player_in:
#        try:
#            stayOrHit = int(input("1: Stay\n2: Hit\n"))
#        except ValueError:
#            print("Please press ether the nr '1' button or nr '2' button and try again")
#           continue
#    if total(dealerHand) > 16:
#        dealer_in = False
#    else:
#        dealCard(dealerHand)
#    if stayOrHit == 1:
#        player_in = False
#   else:
#       dealCard(playerHand)
#   if total(playerHand) >= 21:
#       player_in = False
#   elif total(dealerHand) >= 21:
#        dealer_in = False

#if total(playerHand) == 21:
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("Black Jack! You win")
#    worth += beting * 2
#elif total(dealerHand) == 21:
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("Black Jack! Dealer wins")
#    worth -= beting
#elif total(playerHand) > 21:
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("You Bust! Dealer wins")
#    worth -= beting
#elif total(dealerHand) > 21:
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("Dealer busts! You win")
#    worth += beting * 1.5
#elif 21 - total(dealerHand) < 21 - total(playerHand):
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("You win")
#    worth += beting * 1.5
#elif 21 - total(dealerHand) > 21 - total(playerHand):
#    print(F"\nYou have {playerHand} for a total of {total(playerHand)} an the dealer have {dealerHand} for a total of {total(dealerHand)}")
#    print("Dealer Wins")
#    worth -= beting




#deck 


#betting

#Hand/dator/spelare

#poäng

#winnare/game

#spelare