
import random
import time

points = 100

bet = int(input("what do you bet (only whole numbers): "))

knight = 10

queen = 10

king = 10

ace= 1

#deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 10, J, Q, K, 11]

#deck = [["ace", "spades"], ["2", "spades"]]

spades = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king]
hearts = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king]
clubs = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king]
diamonds = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king]

hand = 0

game = 0

dealer = 0
def refreshnewcard():
    return random.choice(spades or hearts or clubs or diamonds)
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
