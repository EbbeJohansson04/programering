#yatsy

#regler

# 5st 6 sidiga tärningar

# 3 kast per spelare per omgång

# Efter 3 kast väljer spelaren i fråga en poängruta att fylla i

# Poäng betsämms av antalet som matchar kompinationen av vald ruta

# När tabbellen är slut räknas poängen ihop

#POÄNGTABELL:

# 1:or (5)
# 2:or (10)
# 3:or (15)
# 4:or (20)
# 5:or (25)
# 6:or (30)
# Summa
# Bonus (50)    Över 63 = 50 poäng bonus
# Par (12)
# 2par (22)
# Triss (18)
# Fyrtal (24)
# kåk (28)
# liten stege (15)
# stor stege (20)
# chans (30)
# ryatzy (50)


import random

class Dice():
    def _init_(self):
        self.tärning = [1, 2, 3, 4, 5, 6]


    def __str__(self):
        return self.tärning



class Player():
    def _init_(self):
        self.names = input("Your Name? ")
        #if names == "":
        #   name = name.append(input())

class Point_list():
    def _init_(self):
        lista = ["1:or", "2:or", " 3:or", "4:or", "5:or", "6:or", "Par", "2par", "Triss", "Fyrtal", "kåk", "liten stege", "stor stege", "chans", "ryatzy"]

class Play():
    def _init_(self):
        self.dice = Dice()
        self.players = Players()
        self.point_list = Point_list()

        def play(self):
            turn = 0
            choice = input("Play ? yeas or No: ").lower
            while choice == "yes" and turn <= 3:
                