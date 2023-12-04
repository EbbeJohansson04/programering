import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

hand = 0

dealer = 0

def play():
    random.shuffle(deck)
    choice = input("hit or stand: ").lower()
    if choice == "hit":
        hand.append(deck)
        hand.append(deck)
        dealer.append(deck)
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        print(hand)
        
print

print(play())

        
