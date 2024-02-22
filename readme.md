 # Loggbok

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
class BlackJack_game():
    def _init_(self):
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

#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 11]*4



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
            points += bet * 2.5
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
    print("You win!!!!: ", bet * 2, " pointsn")
    print("Your currently have: ", points, " points")  


if hand == dealer and choice == "p":
    print("A Nice Tie :) Insert amount of points  returned here same as inserted")

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


func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		velocity.y += gravity * delta

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
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

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