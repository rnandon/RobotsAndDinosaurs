## Imports
#####################################
import time
from random import randint
from Weapon import Weapon


# Robot. Basics are the same as the dinosaur, but has a weapon, power instead of energy, and only one kind of attack
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 100
        weapons = [Weapon("Sword", randint(15, 25)), Weapon("Axe", randint(10, 30)), Weapon("Stuffed Rabbit", randint(1, 50))]
        self.weapon = weapons[randint(0, len(weapons)-1)]

    # Deal damage to the selected dinosaur if the robot has enough power
    def attack(self, dinosaur):
        if self.power >= 10:
            dinosaur.health -= self.weapon.attack_power
            if dinosaur.health < 0:
                dinosaur.health = 0
            self.power -= 10
            print(f"     {self.name.rstrip()} attacks {dinosaur.name} for {self.weapon.attack_power} damage!")
            time.sleep(1)
        else:
            print(f"     {self.name.rstrip()} doesn't have the power to attack!")
            time.sleep(1)

    # Special formatting for health value
    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    # Special formatting for power value
    def get_power(self):
        if self.power > 99:
            return f'{self.power}'
        if self.power > 9:
            return f'{self.power} '
        if self.power <= 9:
            return f'{self.power}  '
