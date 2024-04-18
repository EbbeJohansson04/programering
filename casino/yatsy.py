import random

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
    def __init__(self):
        self.roll = []

    def roll_dice(self):
        x = 0
        while x > 6:
            z
class Hand():
    #players hand/erned points
    def __init__(self, player_name):
        self.checkbox = []
        self.points = []
        self.name = player_name

    def add(self, checks):
        self.checkbox.append(checks)
        return self.checkbox


class Lista():
    def __init__(self):
        self.lista = ["1:or", "2:or", " 3:or", "4:or", "5:or", "6:or", "Par", "2par", "Triss", "Fyrtal", "kåk", "liten stege", "stor stege", "chans", "ryatzy"]



class Play():
    def __init_(self):
        self.point_list = List()
        self.player_points = Hand("name")
        self.player_turn = 0

    def Play(self):
        play = input("Play. Yes or No ").lower()
        if play == "yes" and self.player_turn <= 3:
            #self.player_points.clear()
            #self.point_list.clear()
            print(point_list)
            print(tärning.roll)
            answer = input("spara något")
            # 1 1 1 4 5 
            # 1 1 1 1 4 
            # 1 1 2 3 4
            #spara separata index i lista och ta bort de som inte sparas vi indexvärde




print("hello")


tärning = Dice()
print(tärning.roll)




    #def play(self):
    #    for i in self.players:
    #        turn = 0
    #        choice = input("Play ? yeas or No: ").lower
    #        while choice == "yes" and turn <= 3:
    #            for i in 5:
    #                roll = []
    #                roll.append.random(self.dice)
    #                print(roll)
    #            x = 1
#
    #            keep = input("Vill du spara något: ").lower()
    #            if keep == "yes":
    #                answer = int(input("Vad will du spara (ett nummer): ")) # 11,1 
#
    #            antal = [-1]
    #            for i in 5:
#
    #                antal.append = roll.count(x)
    #                x =+1
    #            if antal[1] == 3:
    #                break
    #            
#
#
    #                



#class Points():
#    def __init__(self, lista):
#        played = []
#        played = played.append(self.lista) 
#
#        if played == "1:or":
#            self.points =+ 5
#        elif played == "2:or":
#            self.points =+ 10
#        elif played == "3:or":
#            self.points =+ 15
#        elif played == "4:or":
#            self.points =+ 20
#        elif played == "5:or":
#            self.points =+ 25
#        elif played == "6:or":
#            self.points =+ 30
#        elif played == "par":
#            self.points =+ 12
#        elif played == "2par":
#            self.points =+ 22
#        elif played == "triss":
#            self.points =+ 18
#        elif played == "fyrtal":
#            self.points =+ 24
#        elif played == "kåk":
#            self.points =+ 28
#        elif played == "liten stege":
#            self.points =+ 15
#        elif played == "stor stege":
#            self.points =+ 20
#        elif played == "chans":
#            self.points =+ 10
#        elif played == "yatzy":
#            self.points =+ 50
#        else:
#            print("u got nothing")
#
#




#class Hand():
#    def ___init__(self, names):
#        self.dice = []
#        self.name = names
#    
#    def add(self, card):
#        self.lista.append()
#

#
#class Turn():
#    def ___init__(self, turn):
#        self.turn = []
#
#        while turn <= 3:
#            for i in 5:
#                x = random.list
#                turn.append(x)
#
#        def __str__(self):
#            return self.turn
#
#fan = Turn()
#
#print(fan.turn)