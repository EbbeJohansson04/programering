import random

class Dice():
    def __init__(self, faces):
        self._faces = faces

    def get_faces(self):
        return self._faces
        
    def roll_die(self):
        return random.randint(1, self._faces)

dice = Dice(6)

print(dice.roll_die())




def generate_dice(amount, faces):
    dice_list = [Dice(faces) for die in range(amount)]
    return dice_list



def roll(dice):
    values = [die.roll_die() for die in dice]
    for die in values:
        print(die, end=" ")
    print(f'\nsum of rolled dice = {sum(values)}')
    return values

our_dice = generate_dice(5, 6)
roll(our_dice)

def main():
    dice_face = int(input("nr of sides: "))
    dice_amount = int(input("nr of dice: "))

    my_dice = generate_dice(dice_amount, dice_face)
    print("press q to quit: ")

    roll_input = ''
    while roll_input != 'q':
        roll_dice = roll(my_dice)
        roll_input = input("roll or q: ")
    
if __name__ == '__main__':
    main()
