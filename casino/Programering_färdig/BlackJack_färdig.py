
import random


#fler spelare#


#playerin = True
#dealerin = True

#worth = 100

#beting = int(input("How much do dare to bet: "))


class Betin():
    def __init__(self) -> None:
        self.worth = 100
        self.beting = int(input("How much do dare to bet: "))

class Deck():
    def __init__(self)-> str:
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A",  "J", "Q", "K", "A",  "J", "Q", "K", "A", ]
        self.playerHand = []
        self.dealerHand = []

        return self.dealerHand

class Hand():
    def __init__(self, card,) -> None:
        self.card = card
#        self.turn = turn
        self.turn = []
    
    def dealCard(self, deck):
        self.card = random.choice(deck)
        self.turn.append(self.card)
        self.deck.remove(self.card)

    def __init__(self) -> None:
        self.hand = []
        
    def giveCards(self):
        for _ in range(2):
            self.dealCard(self.dealerHand)
            self.dealCard(self.playerHand)



class Points():
    def __init__(self) -> None:
        self.total = 0
        self.face = ["J", "Q", "K"]
    
    def total(self, turn) -> int:
        for self.card in turn:
            if self.card in range(1, 11):
                self.total += self.card
            elif self.card in self.face:
                self.total += 10
            else:
                if self.total > 11:
                    self.total += 1
                else:
                    self.total += 11
        return self.total





class Dealer():
    def __init__(self) -> None:
        self.hand = []

    def revealDealerHand(self):
        if len(self.dealerHand) == 2:
            return self.dealerHand[0]
        elif len(self.dealerHand) > 2:
            return self.dealerHand[1]



class Player():
    def __init__(self) -> None:
        self.hand = []


class Play():
    def __init__(self) -> None:
        self.playerin = True
        self.dealerin = True
        self.stayOrHit = 0
        self.dealerHand = []
        self.playerHand = []


    
    def game(self):
        while self.playerin or self.dealerin:
            print(F"Dealer has {self.dealerHand()} and x")
            print(f"You have {self.playerHand}  for a total of {self.total(self.playerHand)}")
        if self.playerin:
            self.stayOrHit = input("1: Stay\n2: Hit\n")
            if self.stayOrHit.isdigit():
                int(self.stayOrHit)
            else:
                print("Please press ether the nr '1' button or nr '2' button and try again")
        if self.total(self.dealerHand) > 16:
            self.dealerin = False
        else:
            self.dealCard(self.dealerHand)
        if self.stayOrHit == 1:
            self.playerin = False
        else:
            self.dealerCard(self.playerHand)
        if self.total(self.dealrHand) >= 21:
            self.dealerin = False
        if self.total(self.playerHand) >= 21:
            self.playerin = False

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

#while playerin or dealerin:
#    print(F"Dealer has {revealDealerHand()} and x")
#    print(f"You have {playerHand}  for a total of {total(playerHand)}")
#    if playerin:
#        try:
#            stayOrHit = int(input("1: Stay\n2: Hit\n"))
#        except ValueError:
#            print("Please press ether the nr '1' button or nr '2' button and try again")
#           continue
#    if total(dealerHand) > 16:
#        dealerin = False
#    else:
#        dealCard(dealerHand)
#    if stayOrHit == 1:
#        playerin = False
#   else:
#       dealCard(playerHand)
#   if total(playerHand) >= 21:
#       playerin = False
#   elif total(dealerHand) >= 21:
#        dealerin = False

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