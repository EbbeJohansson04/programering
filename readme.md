 # Loggbok
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


Utöver detta har jag blrjad "värma upp" inför ett mindre project där jag ska göra ett digitalt casino där man kan spela olika klassiska casino spel.

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