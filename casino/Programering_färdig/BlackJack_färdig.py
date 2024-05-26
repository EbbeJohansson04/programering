
import random

playerin = True
dealerin = True


#deck of cards / player dealer hand

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A",  "J", "Q", "K", "A",  "J", "Q", "K", "A", ]
playerhand = []
dealerhand = []

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)



def total(turn):
    total = 0
    face = ["J", "K", "Q"]
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else: 
            if total > 11:
                total += 1
            else: total += 11
    return total


def revealDealerHand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len (dealerhand) > 2:
        return dealerhand[0], dealerhand[1]
    


for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)



while playerin or dealerin:
    print(F"Dealer has {revealDealerHand()} and x")
    print(f"You have {playerhand}  for a total of {total(playerhand)}")
    if playerin:
        try:
            stayOrHit = int(input("1: Stay\n2: Hit\n"))
        except ValueError:
            print("Please press ether the nr '1' button or nr '2' button and try again")
            continue
    if total(dealerhand) > 16:
        dealerin = False
    else:
        dealcard(dealerhand)
    if stayOrHit == "1":
        playerin = False
    else:
        dealcard(playerhand)
    if total(playerhand) >= 21:
        playerin = False
    elif total(dealerhand) >= 21:
        dealerin = False

if total(playerhand) == 21:
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("Black Jack! You win")
elif total(dealerhand) == 21:
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("Black Jack! Dealer wins")


elif total(playerhand) > 21:
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("You Bust! Dealer wins")
elif total(dealerhand) > 21:
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("Dealer busts! You win")


elif 21 - total(dealerhand) < 21 - total(playerhand):
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("Dealer Wins")
elif 21 - total(dealerhand) > 21 - total(playerhand):
    print(F"\nYou have {playerhand} for a total of {total(playerhand)} an the dealer have {dealerhand} for a total of {total[dealerhand]}")
    print("Dealer Wins")