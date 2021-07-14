## Imports
######################################
import time
from random import randint


# Dinosaur. Basics are the same as the robot, but it has its own attack power, energy instead of power, and has multiple attacks to choose from 
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 100
        self.attack_names = ("Swipe", "Slash", "Stomp")

    # Deal damage to selected robot if dinosaur has enough energy 
    def attack(self, robot):
        if self.energy >= 10:
            attack = self.attack_names[randint(0, len(self.attack_names) - 1)]
            robot.health -= self.attack_power
            self.energy -= 10
            print(f"     {self.name.rstrip()} attacks {robot.name} with {attack} for {self.attack_power} damage!")
            time.sleep(1)
        else:
            print(f"     {self.name.rstrip()} doesn't have the energy to attack!")
            time.sleep(1)

    # Special formatting for health value
    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    # Special formatting for energy value
    def get_energy(self):
        if self.energy > 99:
            return f'{self.energy}'
        if self.energy > 9:
            return f'{self.energy} '
        if self.energy <= 9:
            return f'{self.energy}  '
