
import random

class Player():
    def __init__(self, name):
        self.name = []
        self.name.append(input("name of player "))

class Dice():
    def __init__(self):
        self.die = []
        self.number_of_dice = []
  #      for i in range (choice):
        for i in range(len(self.number_of_dice)):
            self.die.append(random.randint(1, 6))



class Table():

    def __init__(self):
        self.table = ["1:or", "2:or", " 3:or", "4:or", "5:or", "6:or", "Par", "2par", "Triss", "Fyrtal", "kåk", "liten stege", "stor stege", "chans", "ryatzy"]
        for choice in table:
           if choice == 


class Point():

    def __init__(self):
        self.points_1 = []
        self.points_2 = []
        self.points_1_total = sum(self.points_1)
        if self.points_1_total >= 63:
            self.points_1_total += 50
        


class Hand():
    #players hand/erned points
    def __init__(self):
        self.checkbox = []
        self.points = []


class Lista():
    def __init__(self):
        self.lista = ["1:or", "2:or", " 3:or", "4:or", "5:or", "6:or", "Par", "2par", "Triss", "Fyrtal", "kåk", "liten stege", "stor stege", "chans", "yatzy"]



class Play():
    def __init__(self):
        self.tärning = Dice()
        self.number = []
        self.saved = []

        print(self.tärning.die)


    def start(self):
        # slår tärning
        #sortera tärningarna i numerordning
        self.tärning.die.sort()
        print(self.tärning.die)

        # Kolla om spelaren har slagit yatzee
        if self.tärning.die[0] == self.tärning.die[-1]:
            print("You Got Yatzee 50 points:")

        #kollar om spelaren slagit par
        for i in range(len(self.tärning.die)):
            for i in range(6):
                if self.tärning.die[i] == self.tärning.die[i + 1]:
                    if self.tärning.die[i] == 1:
                        pass
                        #par i 1:or
                    if self.tärning.die[i] == 2:
                        pass
                        #par i 2:or
                    if self.tärning.die[i] == 3:
                        pass
                        #par i 3:or
                    if self.tärning.die[i] == 4:
                        pass
                        #par i 4:or
                    if self.tärning.die[i] == 5:
                        pass
                        #par i 5:or
                    if self.tärning.die[i] == 6:
                        #par i 6:or
                        pass
            

        
                
        #if self.tärning.die[i] == self.tärning.die[i + 1] and self.tärning.die[i + 1] == 
        #kollar antalet par/ triss





        # Kolla om första slaget kan ge poäng
        A = "no"
#        A = input("Do you want to save something: ").lower
 



game = Play()
game.start()

