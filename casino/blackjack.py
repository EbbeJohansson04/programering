
import random
import time


J = 10

Q = 10

K = 10

#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 11]*4

deck = [5, 6, K]

hand = 0

game = 0

dealer = 0

choice = input("play or not?: ")

keep_going = 0

if choice == "p":
        hand += random.choice(deck)
        print("Your hand: ", hand)
        time.sleep(1.5)
        dealer += random.choice(deck)
        print("Dealers hand: ", dealer)
        time.sleep(1.5)
        hand += random.choice(deck)
        print("Your hand: ", hand)
        print("Dealers hand: ", dealer)
        if hand == 21:
            print("You got a BlackJack")
            points += * 1,5
            game = "ended"
        else:
            keep_going = input("hit or stand: ")
            while keep_going == "hit" and game != "ended":
                hand += random.choice(deck)
                if hand < 21:
                    print("Your hand: ", hand)
                    keep_going = input("hit or stand: ")
                else: break
            while dealer <= 17:
                dealer += random.choice(deck)
else:
    print("Try Again and Learn To Spell You Damn Monkey")


if hand > 21:
    print("You Got Fat and lose with a hand of", hand)
    print("Insert amount of points lost here")
if dealer > 17 and hand > dealer:
    print("You win!!!!!  Insert amount of points won here")

if hand == dealer and choice == "p":
    print("A Nice Tie :) Insert amount of points  returned here")





 
 #   _____
 #   |   |
 #   |   |
 #   |   |
 #   |   |_____
 #   |         |
 #   |_________|
#
#
 #   _________________
 #   ----------------
 #   |              |
 #   |    ------    |
 #   |   |      |   |
 #   |   |      |   |
 #   |    ------    |
 #   |              |
 #   ----------------
#
#
 #   ------------
 #   |    ------    |
 #   |    ------    |
 #   |    ------    |
 #   |    ------    |
 #   ------------
 #   |    ------    |
 #   |    ------    |
 #   |    ------    |
 #   |    ------    |
#

