import random

# Wordle med python

# Bestäm ett ord från lista

# Ge antal chanser

# Gör att man kan gissa

# Kolla om rätt eller fel

# avslut



#class wordle():
#
#    wotd = ["kaka", "kossa", "skola", "stekpanna", "wodka", "bil", "träd"]
#    word = 1
#    
#
#joel = wordle
#
#print(joel.word)



class Word():

    def __init__(self):
        self.kaka = ["kaka", "kossa", "skola", "stekpanna", "bil", "träd"]
        self.word = random.choice(self.kaka)


    def __str__(self):
        return self.word
        

wotd = Word()


class Display():

    def __init__(self):
        self.dis = []
        for i in self.word:
            self.dis.append("_")
            return self.dis



        


print("What is the Word of The Day?")

print("Guess One Letter At A Time Untill You Figure It out")


length = len(wotd.word)


print(length)




x = ["h", "u", "s", "b", "i", "l"]

y = ["_","_","_","_","_" ]

for letter, val in enumerate(x):
    if val == "s":
        print((letter ))