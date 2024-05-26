import random

#loldle fast med personer från skolan

#kategorierna är

#roll

#ålder/födelseår

#avdelning





class Word():

    def __init__(self):
        self.kaka = ["kaka", "kossa", "skola", "stekpanna", "bil", "träd"]
        self.word = random.choice(self.kaka)


    def __str__(self):
        return self.word
        

wotd = Word()


length = len(wotd.word)


print(length)
print(wotd)

class Person():

    def __init__(self):
        self.list = ["Anna", "Joel", "Kenneth", "Rikard", "Nils"]
        self.person = random.choice(self.list)

    def __str__(self):
        return self.person

fan = Person()

le = len(fan.person)

print(le)
print(fan)