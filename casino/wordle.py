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
        

motd = Word()


print("What is the Word of The Day?")

print("Guess One Letter At A Time Untill You Figure It out")


length = len(motd.word)


print(length)


if length == 10:
    print("_ _ _ _ _ _ _ _ _ _")
elif length == 9:
    print("_ _ _ _ _ _ _ _ _")
elif length == 8:
    print("_ _ _ _ _ _ _ _")
elif length == 7:
    print("_ _ _ _ _ _ _")
elif length == 6:
    print("_ _ _ _ _ _")
elif length == 5:
    print("_ _ _ _ _")
elif length == 4:
    print("_ _ _ _")
elif length == 3:
    print("_ _ _")
elif length == 2:
    print("_ _")
    


guess = input("Guess One Letter: ")




for i in motd.word:
    if 

x = "KAKA"

print(x[0] )



print(motd.word)