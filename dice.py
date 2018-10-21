# Script Name	: dice.py
# Author		: Yaseen
# Created		: 05th February 2018
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: This will randomly select two numbers,
# like throwing dice, you can change the sides of the dice if you wish

import random


class Dice(object):
    # A dice has a feature of number about how many sides it has when it's
    # established,like 6.
    def __init__(self):
        self.sides = 6

    """because a dice contains at least 4 planes.
    So use this method to give it a judgement when you need
    to change the instance attributes.
    """
    def set_sides(self, sides_change):
        if sides_change >= 1:
            "if slide is greater than sides_change"
            if sides_change != 6:
                print("change sides from 6 to ", sides_change, " !")
            else:
                # added else clause for printing a message that sides set to 6
                print("sides set to 6")
            self.sides = sides_change
        else:
            print("wrong sides! sides set to 6")

    def roll(self):
        return random.randint(1, self.sides)


d = Dice()
d1 = Dice()
d.set_sides(4)
d1.set_sides(4)
print(d.roll(), d1.roll())
