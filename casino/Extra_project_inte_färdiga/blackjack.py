
import random
import time

points = 100

bet = int(input("what do you bet (only whole numbers): "))

knight = 10

queen = 10

king = 10

ace= 1

#class black_jack():
#
#    class card():
#        def _init_(self, suit, value):
#            self.suit = suit
#            self.value = value
#
#        def __str__(self):
#                as_string = ""
#                if self.value == 1:
#                    as_string += 'A'
#                elif self.value == 10:
#                    as_string += 'J'
#                elif self.value == 10:
#                    as_string += 'D'
#                elif self.value == 10:
#                    as_string += 'K'
#                else:
#                    as_string += str(self.value)
#                as_string += self.suit
#                return as_string
#
#        def _repr_(self):
#            return str(self)
#
#    class deck():
#        def _init__(self):
#            self.cards = []
#            self.create_deck()
#            self.shuffle()
#
#        def new_deck(self):
#            self.cards = []
#            for i in range(1,14):
#                self.card.append(Card('\u2660', i))
#                self.card.append(Card('\u2665', i))
#                self.card.append(Card('\u2666', i))
#                self.card.append(Card('\u2663', i))
#
#            def print(self):
#                print(self.cards)
#
#            def print(self):
#                random.shuffle(self.cards)
#
#            def draw_card(self):
#                card = self.cards.pop()
#                return cad
#
#
#
#    class hand():
#        def _init_(self, player):
#            self.cards = []



spades = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
hearts = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
clubs = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
diamonds = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]



hand = 0

game = 0



#    dealer = 0
#    def refreshnewcard():
#        return random.choice(spades or hearts or clubs or diamonds)

choice = input("play or not?: ")
keep_going = 0
if choice == "play":
    newcard = refreshnewcard()
    hand += newcard
    print("Your Hand: ", hand)
    time.sleep(1.5)
    newcard = refreshnewcard()
    dealer += newcard
    print("Dealers Hand: ", dealer)
    time.sleep(1.5)
    hand += random.choice(spades or hearts or clubs or diamonds)
    print("Your Hand: ", hand)
    print("Dealers Hand: ", dealer)
    if hand == 21:
        print("You Got a BlackJack")
        points += 1,5
        game = "ended"
    else:
        keep_going = input("Hit or Stand: ").lower()
        while keep_going == "Hit" and game != "ended" and hand < 21:
            hand += random.choice(spades or hearts or clubs or diamonds)
            if hand < 21:
                print("Your Hand: ", hand)
                keep_going = input("Hit or Stand: ")
        while dealer <= 17:
            dealer += random.choice(spades or hearts or clubs or diamonds)
            print("Dealers Hand: ", dealer)
elif choice == "not":
    print("Lets Play Another Time Then :)")
    break
else:
    print("Learn To Spell You Damn Monkey And Try Again Later")
if hand > 21:
    points -= bet
    print("You Got Fat and lose With a Hand of", hand)
    print("Your Lose Your Bet.")
    print("Your Currently Have: ", points - bet, " Points")
if dealer < hand and hand <= 21:
    print("You Win!!!!: ", bet * 2, " Points")
    print("Your Currently Have: ", points + bet, " Points")  
if dealer > hand and dealer <= 21:
    print("You Lose. The Dealer wins")
    print("Your Lose Your Bet.")
    print("Your Currently Have: ", points - bet, " Points")
if hand == dealer and choice == "p":
    print("A Nice Tie :) Insert amount of points  returned here same as inserted")
