## Imports
######################################
from Combatant import Combatant
from random import randint


# Dinosaur. Basics are the same as the robot, but it has its own attack power, energy instead of power, and has multiple attacks to choose from 
class Dinosaur(Combatant):
    def __init__(self, name, attack_power, energy=100):
        self.attack_names = ("Swipe", "Slash", "Stomp")
        super(Dinosaur, self).__init__(name, attack_power, energy)

    ###        METHODS
    ### ===========================================================
    def attack(self, opponent):
        # Call the combatant attack method, then return damage and attack name for the user interface to use
        attack_name = self.attack_names[randint(0, len(self.attack_names) - 1)]
        damage_dealt = super(Dinosaur, self).attack(self, opponent)
        return (damage_dealt, attack_name)