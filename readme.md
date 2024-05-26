# Loggbok

### Vecka 21

## Lördag
Gör nu ett snabbt och enkelt Black Jack spel (ej Object orienterat). Funkar inte riktigt än men funkar så länge man inte vill sluta få kort. OBS! Vill du se objectorienterat se filen crypto.py eller virus.py ( inget virus förrän komentarerna tas bort samt är inget virus utan gör bara att ett fönster poppar upp. Stäng av programet så slutar det.) 

## Lördag
Jag har en del panik och kommer inte hinna klart med projectet. Har därför bestämt mig för att inte göra det ombjectorienterat utan försöka hinna klart och göra projectet i "vanlig" programering.

### Vecka 16

## Måndag

Har haft problem med package.json och har därför inte kunnat skriva så mycket kod eftersom jag inte har kunnat köra den. Spenderade majoriteten av lektionen med att försöka fixa prorblemet men tror jag får löst det tills nästa lektion.

### Vecka 15

## Trosdag

Idag har det gått segt då jag har hållit på att göra ett bättre flödeschema för yatzy programmet då jag fastnad med vad jag skulle göra. Utöver detta har jag börjat göra om koden så den funkar för fler spelare men fram mot slutet på lektionen kom jag på att det nog skulle vara bättre att göra så koden fungerar för en spelare först. Det svåra med idag var att komma igång samt försöka klura hur jag ska skriva koden. Se bilderna flödesschema 1 & 2.

Koden:

    class Player():
        def __init_(self):
            self.names = []
            answer = int(input("Hur många spelare: "))
            for i in answer:
                self.names = input("Your Name? ")
            return names

    class Play():
        def __init_(self):
            self.dice = Dice("dice")
            self.players = Player("names")
            self.point_list = List("lista")

        def play(self):
            for i in self.players:
                turn = 0
                choice = input("Play ? yeas or No: ").lower
                while choice == "yes" and turn <= 3:
                    for i in 5:
                        roll = []
                        roll.append.random(self.dice)
                        print(roll)

## Onsdag

Idag har jaggjort lite programering i samband med en uppgift i nätverkssäkerheten. Jag skapade en crypteringskod som låter användaren cryptera eller decryptera medelanden med hjälp av ett så kallar cesar cipher. Det svåraste med denna kod var att koma på medelandet skulle crypteras beroende på den nyckeln man vill använda samt bestämma hur looparna skulle cryptera enligt cipherets regler. (se filen med virus och crypto)

Koden:

    def Encrypt(message, key):
        if key == 0:
            new = alphabet
        elif key > 0:
            one = alphabet[:key]
            two = alphabet[key:]
            new = two + one

        encrypted = ""

        for char in message:
            if char == '':
                encrypted += " "
            else :
                for i in range(len(new)):
                    if char == alphabet[i]:
                        encrypted += new[i]
                        break
                else:
                    encrypted += char

        return encrypted

    def Decrypt(encrypted_message, key):
        decrypted = ""
        for char in encrypted_message:
            if char == ' ':
                decrypted += " "
            else:
                index = alphabet.find(char)
                decrypted_char_index = (index - key) % len(alphabet)
                decrypted += alphabet[decrypted_char_index]
        return decrypted



    def kola(medelande, nyckel):
        kola = ""
        for char in medelande:
            if char == ' ':
                kola += " "
            else:
                index = alphabet.find(char)
                kola_char_index = (index - nyckel) % len(alphabet)
                kola += alphabet[kola_char_index]
        return kola

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    answer = input("Encrypt or Decrypt: ").lower()

    x = ""

    if answer == "encrypt":
        message = input("message pls: ").lower()
        key = int(input("shift nr? "))
        x = "yes"
    elif answer == "decrypt":
        medelande = input("message pls: ").lower()
        nyckel = int(input("shift nr? "))
        x = "no"
    else:
        print("U Smort")


    if x == "yes":
        encrypted_message = Encrypt(message, key)
        print("Encrypted: ", encrypted_message)

        dencrypted_message = Decrypt(encrypted_message, key)
        print("Decrypted: ", dencrypted_message)

    elif x == "no":
        fan = kola(medelande, nyckel)
        print("Decrypted: ", fan)

## Måndag

idag har jag fortsatt med mitt yatzy spel och har försökt skapa den del av koden som ansvarar för själva spelandet men det gick inte så jätte bra. Mängden av tiden spenderade jag med att försöka komma på hur jag ska göra det möjligt att ta reda på mängden av de olika siffrorna som täningarna visar samt hur jag sedan skulle göra förr att mängden och kombinationen av olika siffror ska representera olika mål i listan som därefter ska tas bort.

Koden:

class Play():
def _init_(self):
self.dice = Dice("dice")
self.players = Player("names")
self.point_list = List("lista")

    def play(self):
        turn = 0
        choice = input("Play ? yeas or No: ").lower
        while choice == "yes" and turn <= 3:
            for i in 5:
                roll = []
                roll.append.random(self.dice)
            x = 1
            antal = [-1]
            for i in 5:

                antal.append = roll.count(x)
                x =+1
            if antal[1] == 3:

class Points():
def **init**(self, lista):
played = []
played = played.append(self.lista)

        if played == "1:or":
            self.points =+ 5
        elif played == "2:or":
            self.points =+ 10
        elif played == "3:or":
            self.points =+ 15
        elif played == "4:or":
            self.points =+ 20
        elif played == "5:or":
            self.points =+ 25
        elif played == "6:or":
            self.points =+ 30
        elif played == "par":
            self.points =+ 12
        elif played == "2par":
            self.points =+ 22
        elif played == "triss":
            self.points =+ 18
        elif played == "fyrtal":
            self.points =+ 24
        elif played == "kåk":
            self.points =+ 28
        elif played == "liten stege":
            self.points =+ 15
        elif played == "stor stege":
            self.points =+ 20
        elif played == "chans":
            self.points =+ 10
        elif played == "yatzy":
            self.points =+ 50
        else:
            print("u got nothing")

### Vecka 13

## Måndag

Idag har jag bestämt mig för att försöka göra ett Yatzy spel på en högre niv (objekt orientering och liknande). Denna kod ska jag försöka göra klart innan lovet och under lovet ska jag försöka börja lära mig ett nytt språk så som c++ eller liknande. Det nya språket ska jag försöka hålla på med även efter lovet.

Exempel kod:
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

# Bonus (50) Över 63 = 50 poäng bonus

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
#if names == "": # name = name.append(input())

class Point*list():
def \_init*(self):
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

### Vecka 12

Jag har stött på ett problem då jag inte vet vad jag vill göra. Jag kommer på flera ideer som verkar kul att göra men jag får inget driv att göra klart dom då jag tröttnar innan jag blir klar eller efter lektionens slut. Slutade med att jag bestämde mig för att göra ett "virus"

Exempel kod:
import random
from tkinter import \*
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
while True:
win = Toplevel(root)
win.geometry("450x450+{}+{}".format(str(randint(0, root.winfo_screenwidth() - 500)), str(randint(0, root.winfo_screenheight() - 500))))
win.overrideredirect(1)
Label(win, text ="looooooooooooooool!", fg="red").place(relx=.38, rely=.3)
win.lift()
win.attributes("-topmost", True)
win.attributes("-topmost", False)
root.lift()
root.attributes("-topmost", True)
root.attributes("-topmost", False)

threading.Thread(target=placewindows).start()

root.mainloop()

### Vecka 11

Jag har glömt skriva i loggboken men jag har försökt komma på och börja med olika "spel" som jag kan göra.

Exempel kod:
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

### Vecka 10

## måndag - Tisdag

Jag kommer inte på vad mer jag ska göra med BlackJack koden då jag är typ klar samt vill fortsätta med mitt "kasino". Jag har nu börjad med ett wordle spel där man gissar på dagens ord. Det som har varit svårast än så länge var att komma på och implementera kod som visar de bokstäver man gissatt rätt på medan resterande bokstäver visas som \_\_\_\_. Glömde spara så all kod är inte kvar

kod:
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

### Vecka 8

## Tisdag

Idag har jag fortsatt med att fixa upp Rikards kod så den är mer tydlig för spelaren (som ett spel borde vara) Utöver detta har jag även fortsatt med att göra min egen kod objectorienterad.

Exempelkod:

                print("Dealers hand: ", self.computer_hand)
                print(self.player_N," hand: ", self.player_hand)

                k_g = input("Hit or Stand: ").lower
                while k_g == "hit":
                    self.player_hand.add(self.deck.draw_card())
                    print("Yyour Hand: ",self.player_hand)
                    k_g = input("Hit or Stand: ").lower

                while self.computer_hand.sum() < 18:
                    self.computer_hand.add(self.deck.draw_card())
                    print("Dealers Hand: ", self.computer_hand)
                    time.sleep(1)

                #who wins?

                if self.player_hand.sum() > self.computer_hand.sum() and player_hand.sum() <= 21:
                    print(self.player_N, " Wins!")
                elif self.player_hand.sum() == self.computer_hand.sum():
                    print("It Is A Nice Tie!")
                elif self.player_hand.sum() < self.computer_hand.sum() and self.computer_hand() <= 21:
                    print("You Lose, Better Luck Next Time!")
                else:
                    print("What Happened?")

## Måndag

Denna dag har jag försökt fixa upp koden för delen som är ansvarig för själva spelet samt gör om min kod till att bli mer baserad på klasser liksom Rikards kod.

Exempel på kod:
class BlackJack*game():
def \_init*(self):
self.deck = Deck()
self.player_hand = Hand("Player")
self.computer_hand = Hand("Computer")

        def play(self):
            choice = input("Play? yes or no: ")
            while choice == "yes":
                self.layer_hand.clear()
                self.computer_hand.clear()

                self.player_hand.add(self.deck.draw_card())
                self.player_hand.add(self.deck.draw_card())

                self.computer_hand.add(self.deck.draw_card())

                print("Dealers hand: ", self.computer_hand)
                print(self.player_N," hand: ", self.player_hand)

### Vecka 6

## Måndag

Har övat på cratch samt har planerat/gjort ett uppläg inför lektionen jag ska hålla på Hallerna skolan.

## Torsdag

Jag har fått hjälp av Joel som har gått igenom hur jag bättre kan använda mig av object inför mitt object orienterade projekt. Kod förekommer vid senare datum

### Vecka 3 - 5

PGA mitt dåliga minne har jag glömt att skriva i loggboken men jag har övat på scratch inför utlärning på Hallerna skolan vecka 6. Jag har gjort lite olika spel av en enklare varriant samt kollat och lekt med lite svprare spel. Kod kan hända att förekomma vid senare datum.

### Vecka 49 - 3

På grund av komplikationer, prov/läxor och det faktum att det var lov så har jag glömt att skriva i loggboken. Under denna tid har jag lagt till ett poäng system som inte är riktigt klart än, jag har skrivit kod som representerar början i vanliga blackjackspel och jag lade till hur dealern fick kort på ett bättre sätt.

För att göra detta möjligt har jag behövt leta reda på några blackjack regler som verkar rimliga.

Dom största problemen jag stött på var att omvandla reglerna till kod. Då det fortfarande är en simpel kod så har det inte varit några större problem än med skrivandet av hur reglerna ska agera när man pelar.

## Min kod:

import random
import time

points = 100

J = 10

Q = 10

K = 10

#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 11]\*4

deck = [5, 6, K]

hand = 0

game = 0

dealer = 0

bet = input("What is your bet?: ")

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
points += bet \* 2.5
game = "ended you won"
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
points -= bet
print("You Got Fat and lose with a hand of", hand)
print("Your lose your bet.")
print("Your currently have: ", points, " points")
if dealer < hand and hand <= 21:
print("You win!!!!: ", bet \* 2, " pointsn")
print("Your currently have: ", points, " points")

if hand == dealer and choice == "p":
print("A Nice Tie :) Insert amount of points returned here same as inserted")

#### Vecka 34 - 44

Ingen loggbok pga komplikationer och byte av opperativsystem som tagit pårt tidigare loggböcker.

### Vecka 46

Idag har jag fixat med det nya operativsystemet och har instalerat VScodium och godot. Utöver detta har jag fixat så jag har en fungerande loggbok och har läst/lärt mig om hur man använder godot engine.

### Vecka 47 - 48

Jag har fortsatt att lära mig om goDot och goDot script enligt https://www.youtube.com/watch?v=UcdwP1Q2UlU&list=LL&index=30 och https://www.youtube.com/watch?v=S8lMTwSRoRg&t=2047s.

Min kod:
extends CharacterBody2D

const SPEED = 110.0
const JUMP_VELOCITY = -300.0

@onready var animated_sprite_2d = $AnimatedSprite2D

# Get the gravity from the project settings to be synced with RigidBody nodes.

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func \_physics_process(delta): # Add the gravity.
if not is_on_floor():
velocity.y += gravity \* delta

    # Handle Jump.
    if Input.is_action_just_pressed("ui_accept") and is_on_floor():
    	velocity.y = JUMP_VELOCITY

    # Get the input direction (input_axis) and handle the movement/deceleration.
    # As good practice, you should replace UI actions with custom gameplay actions.
    var input_axis = Input.get_axis("ui_left", "ui_right")
    if input_axis:
    	velocity.x = input_axis * SPEED
    else:
    	velocity.x = move_toward(velocity.x, 0, SPEED)

    move_and_slide()
    update_animations(input_axis)

func update_animations(input_axis):
if input_axis != 0:
animated_sprite_2d.flip_h = input_axis < 0
animated_sprite_2d.play("run")
else:
animated_sprite_2d.play("idle")
if not is_on_floor():
animated_sprite_2d.play("jump")

Utöver detta har jag börjat "värma upp" inför ett mindre project där jag ska göra ett digitalt casino där man kan spela olika klassiska casino spel.

Min kod än så länge:
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

### Vecka 49

Jag fortsätter med min paus fårn godot med målet om att kunna lämna in ett simplare projekt. denna veckan har jag gjort om min blackjack kod samt skapate ett flödesschema. Bild på flödesschemat saknas då det gjordes på papper men har ingen kamera att ta bild med.

Blackjack kod (som ändrats):
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]\*4

hand = 0

dealer = 0

choice = input("hit or stand: ")

def play(hand, deck):
while hand => 21:  
 if choice == "hit":
hand = random.choice(deck)
else:
hand = "u lose"
return hand

print(play(hand, deck))

Utöver detta har jag även gjort ett simpelt troll virus program i samarbete med nätverkssäkerhets kursen.

# Virus kod:

import webbrowser, random, time

sites =["https://www.youtube.com/watch?v=XHBukBv6Dxc"]

while True:
tabs = random.choice(sites)
webbrowser.open(tabs, new=10)
time.sleep(0.5)
